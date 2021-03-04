import redis
import time
import traceback
from random import randint
from executor import BoundedExecutor, threaded

from queue import Queue, Empty

redis = redis.Redis(host='localhost')

print(redis.execute_command('INFO')['redis_version'])

stream_name = 'mystream'

control_channel = Queue()
values_channel = Queue()

start_time = time.time()
et = 0.0
et_max = 60.0

executor = BoundedExecutor(2, 5)

def format_stacktrace():
    parts = ["Traceback (most recent call last):\n"]
    parts.extend(traceback.format_stack(limit=25)[:-2])
    parts.extend(traceback.format_exception(*sys.exc_info())[1:])
    return "".join(parts)


@threaded(executor)
def do_job_forever(**kwargs):
    try:
        controlQ = kwargs.get('control_channel')
        assert controlQ, 'do_job_forever :: Missing the controlQ.'
        valuesQ = kwargs.get('values_channel')
        assert valuesQ, 'do_job_forever :: Missing the valuesQ.'
        while (controlQ and valuesQ):
            val = randint(0,9999)
            valuesQ.put(val)
            redis.xadd(stream_name, {'message': val})
            try:
                ctrl = controlQ.get_nowait()
            except Empty:
                ctrl = None
            print('\ndo_job_forever :: ctrl -> {}'.format(ctrl))
            if (not ctrl):
                sleep_sec = 5
                print('do_job_forever :: value: %d, sleep: %d sec.' % (val, sleep_sec))
                time.sleep(sleep_sec)
            else:
                break
    except Exception as ex:
        print('do_job_forever :: {}'.format(format_stacktrace()))
    print('do_job_forever terminated.')

    
@threaded(executor)
def show_values_forever(**kwargs):
    try:
        controlQ = kwargs.get('control_channel')
        assert controlQ, 'show_values_forever :: Missing the controlQ.'
        valuesQ = kwargs.get('values_channel')
        assert valuesQ, 'show_values_forever :: Missing the valuesQ.'
        while (controlQ and valuesQ):
            val = valuesQ.get(block=True)
            print('\nshow_values_forever :: show_values_forever :: value: %d' % (val))
            message = redis.xread({stream_name: '$'}, None, 0)
            print('*** show_values_forever :: message -> {}'.format(message))
            try:
                ctrl = controlQ.get_nowait()
            except Empty:
                ctrl = None
            if (ctrl):
                break
            et = time.time() - start_time
            print('\net -> {}'.format(et))
            if (et > et_max):
                controlQ.put_nowait(1)
                break
    except Exception as ex:
        print('show_values_forever :: {}'.format(format_stacktrace()))
    print('show_values terminated.')


do_job_forever(control_channel=control_channel, values_channel=values_channel)
show_values_forever(control_channel=control_channel, values_channel=values_channel)


while (et < et_max):
    print('main-thread :: {} sleeping...'.format(et))
    time.sleep(1)
    et = time.time() - start_time
control_channel.put(1)
control_channel.join()
values_channel.join()

print('Done.')

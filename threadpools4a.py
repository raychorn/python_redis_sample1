import concurrent.futures
from time import sleep, time
from random import randint

from queue import Queue, Empty

control_channel = Queue()
values_channel = Queue()

start_time = time()
et = 0.0
et_max = 30.0

def do_job_forever(**kwargs):
    controlQ = kwargs.get('control_channel')
    assert controlQ, 'Missing the controlQ.'
    valuesQ = kwargs.get('values_channel')
    assert valuesQ, 'Missing the valuesQ.'
    while (controlQ and valuesQ):
        val = randint(0,9999)
        valuesQ.put(val)
        try:
            ctrl = controlQ.get_nowait()
        except Empty:
            ctrl = None
        print('\nctrl -> {}'.format(ctrl))
        if (not ctrl):
            sleep_sec = randint(1, 3)
            print('do_job_forever :: value: %d, sleep: %d sec.' % (val, sleep_sec))
            sleep(sleep_sec)
        else:
            break
    print('do_job_forever terminated.')

    
def show_values_forever(**kwargs):
    controlQ = kwargs.get('control_channel')
    assert controlQ, 'Missing the controlQ.'
    valuesQ = kwargs.get('values_channel')
    assert valuesQ, 'Missing the valuesQ.'
    while (controlQ and valuesQ):
        val = valuesQ.get(block=True)
        print('\nshow_values_forever :: value: %d' % (val))
        try:
            ctrl = controlQ.get_nowait()
        except Empty:
            ctrl = None
        if (ctrl):
            break
        et = time() - start_time
        print('\net -> {}'.format(et))
        if (et > et_max):
            controlQ.put_nowait(1)
            break
    print('show_values terminated.')

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as worker:
    worker.submit(do_job_forever, control_channel=control_channel, values_channel=values_channel)
    worker.submit(show_values_forever, control_channel=control_channel, values_channel=values_channel)

print('Done.')

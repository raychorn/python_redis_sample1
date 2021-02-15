import redis
import time
import datetime


class RedisPub():
    def __init__(self, host='127.0.0.1', port=6379, db=0):
        self.queue = redis.StrictRedis(host=host, port=port, db=db)

    def pub(self, name, value):
        self.queue.publish(name, value)
        

class RedisSub():
    def __init__(self, name, host='127.0.0.1', port=6379, db=0):
        self.queue = redis.StrictRedis(host=host, port=port, db=db)
        self.channel = self.queue.pubsub()

        self.channel.subscribe(name)

    def sub(self):
        message = None
        while (1):
            message = self.channel.get_message()
            if message and (not message['data'] == 1):
                message = message['data'].decode('utf-8')
                break
            time.sleep(0.1)
        return message
        

if (__name__ == '__main__'):
    name = 'chan1'
    value1 = 'Test1'
    s = RedisPub()
    s.pub(name, value1)
    
    p = RedisSub(name)
    m = p.sub()
    assert m == value1, 'Oops, something wrong because we expected {} but got {}.'.format(value1, m)
    print('Got {} which was expected.'.format(m))
    
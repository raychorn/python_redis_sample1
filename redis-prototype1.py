import redis
import datetime

def count_words_at_url(url):
    import requests
    resp = requests.get(url)
    return len(resp.text.split())


def say_hello():
    print('Saying Hello.')
    

if (__name__ == '__main__'):
    if (0):
        r = redis.Redis(host='localhost', port=6379, db=0)
        r.set('foo', 'bar')

        print(r.get('foo'))
        
    if (1):
        from rq import Queue
        q = Queue(connection=redis.Redis())
        result = q.enqueue(count_words_at_url, 'http://nvie.com')
        
        job = q.enqueue_in(datetime.timedelta(seconds=10), say_hello)
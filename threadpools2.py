from bounded_pool_executor import BoundedProcessPoolExecutor
from time import sleep
from random import randint

def do_job(num):
    sleep_sec = randint(1, 10)
    print('value: %d, sleep: %d sec.' % (num, sleep_sec))
    sleep(sleep_sec)

with BoundedProcessPoolExecutor(max_workers=5) as worker:
    for num in range(100):
        print('#%d Worker initialization' % num)
        worker.submit(do_job, num)
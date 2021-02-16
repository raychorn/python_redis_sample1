import sys
import traceback

class threaded(object):
    
    def __init__(self, executor):
        self.executor = executor

    def __call__(self, f):
        try:
            def wrapped_f(*args, **kwargs):
                self.executor.submit(f, *args, **kwargs)
            return wrapped_f
        except Exception as ex:
            extype, ex, tb = sys.exc_info()
            formatted = traceback.format_exception_only(extype, ex)[-1]
            print(formatted)

from concurrent.futures import ThreadPoolExecutor
from threading import BoundedSemaphore


class BoundedExecutor:
    """BoundedExecutor behaves as a ThreadPoolExecutor which will block on
    calls to submit() once the limit given as "bound" work items are queued for
    execution.
    :param bound: Integer - the maximum number of items in the work queue
    :param max_workers: Integer - the size of the thread pool
    
    https://www.bettercodebytes.com/theadpoolexecutor-with-a-bounded-queue-in-python/
    """
    def __init__(self, bound, max_workers, callback=None, callbackArgs=None):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        self.semaphore = BoundedSemaphore(bound + max_workers)
        self.__callback__ = callback if (callable(callback)) else None
        self.__callbackArgs__ = callbackArgs

    """See concurrent.futures.Executor#submit"""
    def submit(self, fn, *args, **kwargs):
        self.semaphore.acquire()
        try:
            future = self.executor.submit(fn, *args, **kwargs)
        except:
            self.semaphore.release()
            raise
        else:
            future.add_done_callback(lambda x: self.semaphore.release())
            return future

    """See concurrent.futures.Executor#shutdown"""
    def shutdown(self, wait=True):
        self.executor.shutdown(wait)
        if (self.__callback__):
            try:
                self.__callback__(self.__callbackArgs__)
            except:
                pass


if (__name__ == '__main__'):
    import time
    sys.path.insert(0, '/workspaces/private-microservices-framework/microservices_framework/python_lib3')
    
    num_done = set()

    def callback(*args, **kwargs):
        print('callback :: args -> {}, kwargs -> {}'.format(args, kwargs))
        print('BEGIN Tests:')
        try:
            assert len(num_done) == total_num, 'Problem #1, Only {} items got done.'.format(len(num_done))
            for i in range(0, total_num):
                assert i in num_done, 'Problem #2, Missing item #{} that seems to have been skipped or not done.'.format(i)
        finally:
            print('END Tests !!!')

    executor = BoundedExecutor(2, 5, callback=callback)

    @threaded(executor)
    def work(num):
        time.sleep(1)
        print('work done for {}.'.format(num))
        num_done.append(num)
        
    total_num = 1000
    for i in range(0, total_num):
        work(i)
        print('work submitted for {}.'.format(i))
    executor.shutdown()

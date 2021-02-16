import sys, traceback
import concurrent.futures


def format_stacktrace():
    parts = ["Traceback (most recent call last):\n"]
    parts.extend(traceback.format_stack(limit=25)[:-2])
    parts.extend(traceback.format_exception(*sys.exc_info())[1:])
    return "".join(parts)


def do_something(something=None):
    print(something)
    return something


somethings = [i for i in range(0, 100)]
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for aThing in somethings:
        futures.append(
            executor.submit(
                do_something, something=aThing
            )
        )
    for future in concurrent.futures.as_completed(futures):
        try:
            print(future.result())
        except Exception as ex:
            print(format_stacktrace())
            
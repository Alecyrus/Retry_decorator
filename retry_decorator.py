import math
import time
import asyncio
import functools
def retry(ignore_exceptions, times=3, base_time=2, block=True, verbose=True):
    """Retry decorator.

    Usage:
        @retry(ignore_exceptions=[ValueError, ], times=3, base_time=2, block=True, debug=True)

    :param ignore_exceptions(list): When the exceptions ares catched, the function decoratored will be retried at a
                                    later time. The default is None.
    :param times(integer): The max retry times. The default is 3.
    :param base_time(integer): Before the function decoratored reteies, it will be sleeped for a calulated time(SLEEP_TIME).
                               SLEEP_TIME = base_time^index, index=[1,2,..., times] The default is 2.
    :param block(boolean): If the value is False, the process of sleep() is non-blocking. The default is True.

    :param verbose(boolean): Assgin it `True` for more verbose output. The default is True.

    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if ignore_exceptions is None:
                    return func(*args, **kwargs)

                for i in range(times+1):
                    try:
                        return func(*args, **kwargs)
                    except tuple(ignore_exceptions) as e:
                        if i == times:
                            if verbose:
                                print("Failed to execute func(%s): retry times reached the upper limit. Exception: %s"
                                      %(func.__name__, str(e.__class__)[8:-2]))
                            raise
                        sleep_time = math.pow(base_time, i+1)
                        if verbose:
                            print("Failed to execute func(%s): wait %d seconds for next retry(%d). Exception: %s"
                                 % (func.__name__, sleep_time, i+1, str(e.__class__)[8:-2]))
                        if block:
                            time.sleep(sleep_time)
                        else:
                            asyncio.sleep(sleep_time)
            except Exception as e:
                raise
        return wrapper
    return decorator




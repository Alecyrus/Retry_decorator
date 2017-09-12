## Retry_decorator
> Language: Python 3.5.2



## Usage
```
>>> form retry_decorator import retry 
>>> help(retry)
Help on function retry in module retry_decorator:

retry(ignore_exceptions, times=3, base_time=2, block=True, verbose=True)
    Retry decorator.
    
    Usage:
        @retry(ignore_exceptions=[ValueError, ], times=3, base_time=2, block=True, debug=True)
    
    :param ignore_exceptions(list): When the exceptions are catched, the function decoratored will be retried at a
                                    later time. The default is None.
    :param times(integer): The max retry times. The default is 3.
    :param base_time(integer): Before the function decoratored reteies, it will be sleeped for a calulated time(SLEEP_TIME).
                               SLEEP_TIME = base_time^index, index=[1,2,..., times] The default is 2.
    :param block(boolean): If the value is False, the process of sleep() is non-blocking. The default is True.
    
    :param verbose(boolean): Assgin it `True` for more verbose output. The default is True.

```

## Example
### Test Function
```python
@retry([ZeroDivisionError], verbose=True)
def div(a,b):
    return a/b
```

> $ python3 simple_test.py
```
The simple test for the Retry Decorator.
The Function for testing:


    @retry([ZeroDivisionError], verbose=True)
    def div(a,b):
        return a/b

    
Output:

Failed to execute func(div): wait 2 seconds for next retry(1). Exception: ZeroDivisionError
Failed to execute func(div): wait 4 seconds for next retry(2). Exception: ZeroDivisionError
Failed to execute func(div): wait 8 seconds for next retry(3). Exception: ZeroDivisionError
Failed to execute func(div): retry times reached the upper limit. Exception: ZeroDivisionError
The exception is catched. division by zero


```






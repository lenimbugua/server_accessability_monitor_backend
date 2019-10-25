import random
import time


def calculate_next_ping_time(func):

    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):

        remaining_duration = 60

        while remaining_duration > 0:
            # storing time before function execution
            print("tick")
            starttime = time.time()
            time.sleep(6.0)
            time_spent = time.time()-starttime
            remaining_duration = remaining_duration-time_spent

            func(*args, **kwargs)

            # storing time after function execution
            end = time.time()
        print("Total time taken in : ", func.__name__, end - starttime)

    return inner1

import time


def measure_execution_time(func):
    def modified_func(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        return result

    return modified_func

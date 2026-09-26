# 12_generators_decorators.py
# Level 1 — Topic 12: Generators, iterators, decorators

import time
from functools import wraps


def countdown(n: int):
    """Simple generator that counts down."""
    while n > 0:
        yield n
        n -= 1


def timer(func):
    """Decorator that prints how long a function took."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper


@timer
def slow_function():
    time.sleep(0.3)
    return "Done"


if __name__ == "__main__":
    print("Countdown:", list(countdown(5)))
    print(slow_function())

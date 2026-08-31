import time


def is_time(func):
    def wrapper(*args, **kwargs):
        '''getting fucntion time'''
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'function: {func.__name__}, time: {end - start:.2f} sec')
        return result
    return wrapper


@is_time
def sum_numbers(numbers):
    return sum(numbers)


res = sum_numbers(range(150000000))
print(res)


@is_time
def say_hello(name):
    print(f"Hello {name}!")

say_hello("Nikita f3+")
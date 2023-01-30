# 1. Sa se implementeze un decorator care masoara timpul necesar executiei unei functii.
import functools
from time import perf_counter, sleep


def function_timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        func(*args, **kwargs)
        stop = perf_counter()
        print(f'{stop - start}')

    return wrapper


@function_timer
def runtime_counter():
    print('Counting the seconds...')


runtime_counter()

print(50 * '#')


# 2. Sa se genereze primele 100 de numere prime
# folosind liste, si apoi folosind generator.
# Comparati diferenta de timp necesara generarii.

@function_timer
def get_odd_numbers(n):
    odd = 1
    odd_list = []
    for i in range(n):
        odd_list.append(odd)
        odd += 2
    print(odd_list)


get_odd_numbers(100)


def get_odd(n):
    generated_number = 0
    current_number = 0
    while generated_number < n:
        if current_number % 2 != 0:
            generated_number += 1
            yield current_number
        current_number += 1


@function_timer
def get_n_odd_numbers():
    emty = []
    for i in get_odd(100):
        emty.append(i)
    print(emty)


get_n_odd_numbers()

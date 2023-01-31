# 1. Sa se implementeze un decorator care masoara timpul necesar executiei unei functii.
import functools
from time import perf_counter


def func_timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        func(*args, **kwargs)
        stop = perf_counter()
        print(stop - start)

    return wrapper


@func_timer
def runtime_counter():
    print('Counting the seconds...')


runtime_counter()

print(50 * '#')


# 2. Sa se genereze primele 100 de numere prime
# folosind liste, si apoi folosind generator.
# Comparati diferenta de timp necesara generarii.

@func_timer
def get_odd_numbers_list(n):
    count = 1
    current = 0
    odd_numbers_list = []

    while count <= n:
        if current % 2 != 0:
            odd_numbers_list.append(current)
            count += 1
            current += 1
        else:
            current += 1
    print(odd_numbers_list)


def get_odd(n):
    generated_number = 0
    current_number = 0
    while generated_number < n:
        if current_number % 2 != 0:
            generated_number += 1
            yield current_number
        current_number += 1


@func_timer
def get_n_odd_numbers_generator(n):
    emty = []
    for i in get_odd(n):
        emty.append(i)
    print(emty)


get_odd_numbers_list(100)
get_n_odd_numbers_generator(100)

print(17 * '=', 'Generator WINS', 17 * '=')

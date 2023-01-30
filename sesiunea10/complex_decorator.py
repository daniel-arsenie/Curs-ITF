# Scrieti un decorator care primeste ca argument
# numele unui fisier si pentru orice functie apelata,
# el va scrie in acel fisier numele functiei,
# lista de argumente ca si string
# si rezultatul apelului.
# Fisierul este de tip csv.
# Functiile decorate pot primi oricate argumente
import csv
import functools


def write_log_in_file(filename):
    def log_message(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func_name = f'{func.__name__}'
            func_args = f'{args, kwargs}'
            func_run = f'{func(*args, **kwargs)}'
            with open(filename, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([func_name, func_args, func_run])

        return wrapper

    return log_message


@write_log_in_file('test.csv')
def a_function_that_returns_a_string():
    return 'a string'


@write_log_in_file('test.csv')
def sum_of_two_numbers(x, y):
    addition = x + y
    return addition


@write_log_in_file('test.csv')
def all_n_numbers(n):
    empty = []
    for i in range(1, n):
        empty.append(i)
    return empty


a_function_that_returns_a_string()
sum_of_two_numbers(x=7, y=9)
all_n_numbers(18)

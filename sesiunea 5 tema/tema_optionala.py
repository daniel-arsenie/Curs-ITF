# 1. Funcție care primește o lună din an și returnează câte zile are acea lună.
print(20 * '-', 'Ex. 1 optional', 20 * '-')

months_and_days = {'Ianuarie': 31,
                   'Februarie ': 29,
                   'Martie': 31,
                   'Aprilie': 30,
                   'Mai': 31,
                   'Junie': 30,
                   'Iulie': 31,
                   'August': 31,
                   'Septembrie': 30,
                   'Octombrie': 31,
                   'Noiembrie': 30,
                   'Decembrie': 31}


def number_of_days_in_month(month):
    for i in months_and_days.keys():
        if i is month:
            return f'{month} are {months_and_days[i]} de zile.'


print(number_of_days_in_month('Iulie'))
print(number_of_days_in_month('Noiembrie'))

# 2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
# împărțirea a două numere.
# În final vei putea face:
# a, b, c, d = calculator(10, 2)

# ● print("Suma: ", a)
# ● print("Diferenta: ", b)
# ● print("Inmultirea: ", c)
# ● print("Impartirea: ", d)
print(20 * '-', 'Ex. 2 optional', 20 * '-')


def multi_purpose_calculator(x, y):
    summ = x + y
    diff = x - y
    multiply = x * y
    division = x / y
    return summ, diff, multiply, division


a, b, c, d = multi_purpose_calculator(20, 4)
print(f'Suma: {a}')
print(f'Diferenta: {b}')
print(f'Inmultirea: {c}')
print(f'Impartirea: {d}')

# 3. Funcție care primește o listă de cifre (adică doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }
print(20 * '-', 'Ex. 3 optional', 20 * '-')

occurencies_dct = {}


def count_occurencies_in_list(lst):
    for i in range(10):
        occurencies_dct[i] = lst.count(i)
    return occurencies_dct.items()


print(count_occurencies_in_list([1, 3, 1, 5, 9, 7, 7, 5, 5]))

# 4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele.
print(20 * '-', 'Ex. 4 optional', 20 * '-')


def biggest_from_3_numbers(a, b, c):
    if a > b and a > c:
        return f'{a} are valoarea maxima dintre cele 3 numere.'
    elif b > a and b > c:
        return f'{b} are valoarea maxima dintre cele 3 numere.'
    return f'{c} are valoarea maxima dintre cele 3 numere.'


print(biggest_from_3_numbers(1, 8, 4))
print(50 * '#')
print(biggest_from_3_numbers(10, 8, 4))
print(50 * '#')
print(biggest_from_3_numbers(1, 8, 40))

# 5. Funcție care să primească un număr și să returneze suma tuturor numerelor
# de la 0 la acel număr.
# Exemplu: dacă dăm numărul 3, suma va fi 6 (0+1+2+3)
print(20 * '-', 'Ex. 5 optional', 20 * '-')


def suma_primelor_n_numere(n):
    if n == 0:
        return 0
    return n + suma_primelor_n_numere(n - 1)


print(suma_primelor_n_numere(5))
print(suma_primelor_n_numere(3))


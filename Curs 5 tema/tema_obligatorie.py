# 1.Funcție care să calculeze și să returneze suma a două numere
print(20 * '-', 'Ex. 1', 20 * '-')


def get_sum_of_2_numbers(a, b):
    result = a + b
    return result


print(get_sum_of_2_numbers(1, 7))
print(50 * '#')
print(get_sum_of_2_numbers(2, -2))

# 2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar
print(20 * '-', 'Ex. 2', 20 * '-')


def even_true_odd_false(n):
    return 'par' if n % 2 == 0 else 'impar'


print(even_true_odd_false(1))
print(50 * '#')
print(even_true_odd_false(2))
print(50 * '#')
print(even_true_odd_false(-8))

# 3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)
print(20 * '-', 'Ex. 3', 20 * '-')


def total_number_of_chars_full_name(nume, prenume, nume_mijlociu):
    chars = list(nume + prenume + nume_mijlociu)
    return len(chars)


nume_intreg = total_number_of_chars_full_name('Daniel', 'Arsenie', 'Oprea')
print(f'Numărul total de caractere din nume este: {nume_intreg}.')
print(50 * '#')
nume_intreg = total_number_of_chars_full_name('Ala', 'Bala', 'Portocala')
print(f'Numărul total de caractere din nume este: {nume_intreg}.')
print(50 * '#')
nume_intreg = total_number_of_chars_full_name('Frone', 'Alexandru', 'Gigel')
print(f'Numărul total de caractere din nume este: {nume_intreg}.')

# 4. Funcție care returnează aria dreptunghiului
print(20 * '-', 'Ex. 4', 20 * '-')


def area_of_rectangle(length, width):
    area = length * width
    return area


total_area = area_of_rectangle(10, 15)
print(f'Aria dreptunghiului este: {total_area}.')
print(50 * '#')
total_area = area_of_rectangle(15, 2)
print(f'Aria dreptunghiului este: {total_area}.')

# 5. Funcție care returnează aria cercului
print(20 * '-', 'Ex. 5', 20 * '-')


def circle_area(r, pi=3.14):
    total_area_circle = pi * (r ** 2)
    return total_area_circle


print(circle_area(7))
print(circle_area(2))

# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
# și False dacă nu găsește.
print(20 * '-', 'Ex. 6', 20 * '-')


def if_char_in_specified_string(n, lst):
    return True if n in lst else False


print(if_char_in_specified_string('a', 'alabala portocala'))
print(if_char_in_specified_string('', 'alabala portocala'))
print(if_char_in_specified_string('a', ''))

# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Numărul de caractere lower case este x
# ● Numărul de caractere upper case exte y
print(20 * '-', 'Ex. 7', 20 * '-')


def count_upper_and_lower_in_string(test):
    count_lower = sum(1 for x in test if x.isupper())
    count_upper = sum(1 for x in test if x.islower())
    print(f'Numărul de caractere lower case este {count_lower}.\n'
          f'Numărul de caractere upper case exte {count_upper}.')


count_upper_and_lower_in_string('Viata Mea de AltaData')
print(30 * '#')
count_upper_and_lower_in_string('Ana nu Are Mereu')

# 8. Funcție care primește o LISTĂ de numere și returnează o LISTĂ doar cu
# numerele pozitive.
print(20 * '-', 'Ex. 8', 20 * '-')


def only_positive_numbers_from_list(list_of_numbers):
    positive_numbers = []
    for number in list_of_numbers:
        if number > 0:
            positive_numbers.append(number)
    return positive_numbers


print(only_positive_numbers_from_list([16, 18, -7, 1, 0, -11, -1]))
print(only_positive_numbers_from_list([-1, -7, 0, -11, -1]))

# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZĂ
# ● Primul număr x este mai mare decat al doilea număr y
# ● Al doilea număr y este mai mare decat primul număr x
# ● Numerele sunt egale.
print(20 * '-', 'Ex. 9', 20 * '-')


def get_which_number_is_greater(x, y):
    if x > y:
        print(f'Primul număr {x} este mai mare decat al doilea număr {y}. ')
    elif y > x:
        print(f'Al doilea număr {y} este mai mare decat primul număr {x}.')
    else:
        print('Numerele sunt egale.')


get_which_number_is_greater(15, 7)
print(10 * '#')
get_which_number_is_greater(-3, 10)
print(10 * '#')
get_which_number_is_greater(12, 12)

# 10. Funcție care primește un număr și un set de numere.
# ● Printează ‘am adaugat numărul nou în set’ + returnează True
# ● Printează ‘nu am adaugat numărul în set. Acesta există deja’ +
# returnează False
print(20 * '-', 'Ex. 10', 20 * '-')


def add_and_check_number_in_set(n, given_set):
    if n in given_set:
        print('Nu am adaugat numărul în set. Acesta există deja.')
        return False
    print('Am adaugat numărul nou în set.')
    return True


print(add_and_check_number_in_set(3, {18, 12, 11, 33, 0}))
print(50 * '#')
print(add_and_check_number_in_set(3, {18, 12, 11, 33, 0, 3}))

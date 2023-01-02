# 1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
# numerele comune.
#
# Exemplu:
# list1 = [1, 1, 2, 3]
#
# list2 = [2, 2, 3, 4]
# Răspuns: {2, 3}
print(20 * '-', 'Ex. 1 Bonus', 20 * '-')


def get_intersection_of_2_lists(lst1, lst2):
    intersect_list = set(lst1) & set(lst2)
    return intersect_list


print(get_intersection_of_2_lists([1, 8, 9, 5, 11], [11, 8, 1, 1, 11, -11, -3]))

# 2. Funcție care să aplice o reducere de preț.
# Dacă produsul costă 100 lei și aplicăm reducere de 10%. Pretul va fi 90 de lei.
# Tratează cazurile în care reducerea e invalidă. De exemplu o reducere de 110%
# e invalidă.

print(20 * '-', 'Ex. 2 Bonus', 20 * '-')


def special_discount(fullprice, discount):
    if discount > 100:
        return 'Reducerea este invalida, te rog incearca din nou.'
    final_price = fullprice - (fullprice * (discount / 100))
    return final_price


print(special_discount(200, 10))
print(50 * '#')
print(special_discount(200, 50))
print(50 * '#')
print(special_discount(200, 101))

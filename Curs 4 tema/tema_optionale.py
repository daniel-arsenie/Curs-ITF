import random

# 1.
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Itereaza prin listă alte_numere
# Populează corect celelalte liste
# Afișează cele 4 liste la final
print(20 * '-', 'Ex. 1 optionale', 20 * '-')

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for numar in alte_numere:
    if numar % 2 == 0:
        numere_pare.append(numar)
    else:
        numere_impare.append(numar)
    if numar < 0:
        numere_negative.append(numar)
    else:
        numere_pozitive.append(numar)

print(f'Numerele pare sunt {numere_pare}.')
print(f'Numerele impare sunt {numere_impare}.')
print(f'Numerele pozitive sunt {numere_pozitive}.')
print(f'Numerele negative sunt {numere_negative}.')

# 2. Aceeași listă:
# Ordonează crescător lista fară să folosești sort.
# Te poți inspira vizual de aici.
# https://www.youtube.com/watch?v=lyZQPjUT5B4
print(20 * '-', 'Ex. 2 optionale', 20 * '-')
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]


def bubble_sort(sortare):
    # Outer loop for traverse the entire list
    for i in range(0, len(sortare) - 1):
        for j in range(len(sortare) - 1):
            if sortare[j] > sortare[j + 1]:
                temp = sortare[j]
                sortare[j] = sortare[j + 1]
                sortare[j + 1] = temp
    return sortare


print("Lista nesortata este: ", alte_numere)
print("Lista sortata este: ", bubble_sort(alte_numere))

# 3. Ghicitoare de număr:
# numar_secret = Generați un număr random între 1 și 30
# Numar_ghicit = None
# Folosind un while
# User alege un număr
# Programul îi spune:
# ● Nr secret e mai mare
# ● Nr secret e mai mic
# ● Felicitări! Ai ghicit!

numar_secret = random.randint(1, 30)
numar_ghicit = None

print(20 * '-', 'Ex. 3 optionale', 20 * '-')

while numar_ghicit != numar_secret:
    numar_ghicit = int(input('Alege un numar:\n'))
    if numar_ghicit > numar_secret:
        print('Nr secret e mai mic')
    elif numar_ghicit < numar_secret:
        print('Nr secret e mai mare')
else:
    print('Felicitări! Ai ghicit!')

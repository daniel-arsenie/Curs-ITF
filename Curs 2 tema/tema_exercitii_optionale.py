# 1.Verifică dacă x are minim 4 cifre (x e int).
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)

x = input('Scrie un numar:\n')

if len(x) <= 3:
    print(f'Ex.1: Numarul {x} nu are minim 4 cifre.')
else:
    print(f'Ex.1: Numarul {x} are minim 4 cifre.')

# 2.Verifică dacă x are exact 6 cifre.

if len(x) == 6:
    print(f'Ex.2: {x} are exact 6 cifre.')
else:
    print(f'Ex.2: {x} nu are 6 cifre.')

# 3. 3.Verifică dacă x este număr par sau impar (x e int).

x = int(x)

if x % 2 == 0:
    print('Ex.3: Numarul este par')
else:
    print('Ex.3: Numarul este impar')

# 4. x, y, z (int)
# Afișează care este cel mai mare dintre ele?

y = int(input('Mai zi-mi un numar: \n'))
z = int(input('Si inca un numar: \n'))

if x > y and x > z:
    print('Ex.4: Primul numar este cel mai mare.')
elif y > x and y > z:
    print('Ex.4: Al doilea numar este cel mai mare.')
elif z > x and z > y:
    print('Ex.4: Al treilea numar este cel mai mare.')
elif x == y == z:
    print('Ex.4: Numerele sunt egale.')
else:
    print('Ex.4: Avem 2 numere cele mai mari.')

# 5. X, y, z - reprezintă unghiurile unui triunghi
# Verifică și afișează dacă triunghiul este valid sau nu.

x_unghi = int(input('Cat sa fie primul unghi al triunghiului?\n'))
y_unghi = int(input('Dar al doilea unghi al triunghiului?\n'))
z_unghi = int(input('Dar al treilea unghi al triunghiului?\n'))

if x_unghi <= 0 or y_unghi <= 0 or z_unghi <= 0:
    print('Ex.5: Un unghi este invalid, mai incearca.')
elif x_unghi + y_unghi + z_unghi <= 180:
    print('Ex.5: Suma unghiurilor este mai mica sau egala cu 180 de grade deci triunghiul este valid.')
else:
    print('Ex.5: Suma unghiurilor este mai mare de 180 de grade deci triunghiul este invalid.')

# 6. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# ● Citește de la tastatură un int x
# ● Afișează stringul fără ultimele x caractere
# Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'

exemplu_6 = 'Coral is either the stupidest animal or the smartest rock'
scadere_cuvant = int(input('Cate litere vrei sa taiem din exemplu?\n'))
scadere_cuvant = -scadere_cuvant

if scadere_cuvant > len(exemplu_6):
    print(f'Prea mult de taiat, incearca un numar mai mic decat {len(exemplu_6)}')
else:
    print(f'Ex.6: "{exemplu_6[0:scadere_cuvant]}"')

# 7. Același string. Declară un string nou care să fie format din primele 5
# caractere + ultimele 5.

primele_caractere = exemplu_6[:5]
ultimele_caractere = exemplu_6[-5:]
exercitiu_7 = primele_caractere + ultimele_caractere
print(f'Ex.7: {exercitiu_7}')

# 8. Același string.
# Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
# este o funcție care te ajuta sa faci asta)
# Folosind această variabilă + slicing, afișează tot stringul până la acest
# cuvânt
# output: 'Coral is either the stupidest animal or the smartest'

index_rock = exemplu_6.index('rock')

print(f'Ex.8: Indexul de start al cuvantului "rock" este {index_rock}.')
print(f'Ex.8: "{exemplu_6[:index_rock]}"')

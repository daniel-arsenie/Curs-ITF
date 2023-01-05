# Exerciții Opționale - grad de dificultate: Mediu spre greu
# (s-ar putea să ai nevoie de Google).
import builtins

# 1. Exercițiu:
# - citește de la tastatură un string de dimensiune impară;
# - afișează caracterul din mijloc.
string_impar = input('Zi-mi ceva mai lung: ')
print(f'Stringul este: {string_impar[0:5]}')
print(f'Caracterul din mijloc este: {string_impar[2]}')

# 2. Folosind o singură linie de cod :
# - citește un string de la tastatură (ex: 'alabala portocala');
# - salvează fiecare cuvânt într-o variabilă;
# - printează ambele variabile pentru verificare.
# print(f'Cele 2 variabile sunt: \n {builtins.input("Scrie 2 cuvinte: ").split()}')

x, y = input("Scrie 2 cuvinte: ").split(); print(x, y)




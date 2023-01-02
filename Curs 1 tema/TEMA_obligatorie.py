'''
Tema 1 - Setup, Variabile, Tipuri de date
Exerciții Recomandate - grad de dificultate: Ușor .
1. Revizualizează întâlnirea 1 și ia notițe în caz că ți-a scăpat ceva.
2. Vizualizează din videoul ‘Primii pași în Programare’:
- Variabile și Tipuri;
- Operatori și Flow Control.
Astfel, la întâlnirea LIVE deja va fi a 2-a oară când vei auzi conceptele și sigur ți
se vor întipări mai bine în minte.
Link: https://www.itfactory.ro/8174437-intro-in-programare/
'''


# Exerciții obligatorii - grad de dificultate: Ușor spre Mediu:
# 1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
# Rezolvare: o variabila este un tip de date care poate stoca valori in memorie

# 2. Declară și initializează câte o variabilă
# din fiecare din următoarele tipuri de variabilă:
# Observație: Valorile vor fi alese de tine după preferințe.

# string
marca = 'Renault'
# int
varsta = 13
# float
km = 179.900
# bool
veche = True

# 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.

print(type(marca))
print(type(varsta))
print(type(km))
print(type(veche))

# 4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
# aceeași variabilă (suprascriere):
km = km.__round__()
print(km)

# - Verifică tipul acesteia.
print(type(km))

# 5. Folosește print() și printează în consolă 4 propoziții folosind cele 4 variabile.
# Rezolvă nepotrivirile de tip prin ce modalitate dorești.
print(f'Am o masina marca {marca}.')
print(f'Este fabricata in 2019 deci are {varsta} ani.')
print(f'Am cumparat-o la 123.000 km si acum are {km} de mii de km.')
print(f'Se poate spune ca este o masina veche? {veche}')

# 6. Citește de la tastatură:
# - numele;
# - prenumele.
numele = input('Care este numele tau de familie? ')
prenumele = input('Care este numele tau de botez? ')

# Afișează: 'Numele complet are x caractere'.
nume_complet = numele + prenumele
print(len(nume_complet))

# 7. Citește de la tastatură:
# - lungimea;
# - lățimea.
lungimea = 12
latimea =11

# Afișează: 'Aria dreptunghiului este x'.
print(f'Aria dreptunghiului este {lungimea * latimea}.')

# 8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
# - afișează de câte ori apare cuvântul 'the';
exemplu = 'Coral is either the stupidest animal or the smartest rock'
print(exemplu.count('the', 14)) # gaseste cuvantul 'the'


# 9. Același string:
# inlocuieste the cu THE peste tot
# printează rezultatul.
print(exemplu.replace('the', 'THE'))

# 10. Același string:
# Folosește un assert ca să verifici dacă acest string conține doar numere.
verificare = str.isdigit(exemplu)
print(f'String-ul conține doar numere? {verificare}')
# 1.Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
# 'Fiat', 'Trabant', 'Opel']
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
# ● Fă același lucru cu un for each.
# ● Fă același lucru cu un while.

print(20 * '-', 'Ex. 1 cu for', 20 * '-')

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
          'Fiat', 'Trabant', 'Opel']
for i in range(len(masini)):
    print(f'Mașina mea preferată este {masini[i]}.')

print(20 * '-', 'Ex. 1 cu for each', 20 * '-')

for masina in masini:
    print(f'Mașina mea preferată este {masina}.')

print(20 * '-', 'Ex. 1 cu for while', 20 * '-')

while len(masini) > 0:
    print(f'Mașina mea preferată este {masini[0]}.')
    masini.pop(0)

# 2. Aceeași listă:
# Folosește un for else
# În for
# - Modifică elementele din listă astfel încât să fie scrise cu majuscule,
# exceptând primul și ultimul.
# În else:
# - Printează lista.

print(20 * '-', 'Ex. 2', 20 * '-')

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
          'Fiat', 'Trabant', 'Opel']

for i in range(1, len(masini) - 1):
    masini[i] = masini[i].upper()
else:
    print(masini)

# 3. Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Iterează prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
# Printează ‘am găsit mașina dorită de dvs’
# Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
# Printează ‘Am găsit mașina X. Mai căutam‘

print(20 * '-', 'Ex. 3', 20 * '-')

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
          'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == "Mercedes":
        print('Am găsit mașina dorită de dvs.')
        break
    else:
        print(f'Am găsit mașina {masina}. Mai căutăm.')

# 4. Aceeași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
# excepția Trabant și Lăstun.
# - Dacă mașina e Trabant sau Lăstun:
# Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
# else).
# - Printează S-ar putea să vă placă mașina x.

print(20 * '-', 'Ex. 4', 20 * '-')

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
          'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina in 'Trabant, Lăstun':
        continue
    print(f'S-ar putea să vă placă mașina {masina}.')

# 5. Modernizează parcul de mașini:
# ● Crează o listă goală, masini_vechi.
# ● Iterează prin mașini.
# ● Când găsesti Lăstun sau Trabant:
# - Salvează aceste mașini în masini_vechi.
# - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# ● Printează Modele vechi: x.
# ● Modele noi: x.

print(20 * '-', 'Ex. 5', 20 * '-')

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
          'Fiat', 'Trabant', 'Opel']
masini_vechi = []

for i in range(len(masini)):
    if masini[i] in 'Lăstun, Trabant':
        masini_vechi.append(masini[i])
        masini[i] = 'Tesla'
print(f'Modele vechi: {masini_vechi}')
print(f'Modele noi: {masini}')

# 6. Având dict:
# pret_masini = {
# 'Dacia': 6800,
# 'Lăstun': 500,
# 'Opel': 1100,
# 'Audi': 19000,
# 'BMW': 23000
# }
# Vine un client cu un buget de 15000 euro.
# ● Prezintă doar mașinile care se încadrează în acest buget.
# ● Iterează prin dict.items() și accesează mașina și prețul.
# ● Printează Pentru un buget de sub 15000 euro puteți alege mașină
# xLastun
# ● Iterează prin listă.

print(20 * '-', 'Ex. 6', 20 * '-')
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
for key, value in pret_masini.items():
    if value < 15000:
        print(f'Pentru un buget de sub EUR 15000 puteți alege mașina {key}la pretul de EUR {value}.')

# 7. Având lista:
# numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterează prin ea.
# ● Afișează de câte ori apare 3 (nu ai voie să folosești count).

print(20 * '-', 'Ex. 7', 20 * '-')

count = 0
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

for numar in numere:
    if numar == 3:
        count += 1
print(count)

# 8. Aceeași listă:
# ● Iterează prin ea
# ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).

print(20 * '-', 'Ex. 8', 20 * '-')

suma = 0
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for numar in numere:
    suma += numar
print(suma)

# 9. Aceeași listă:
# ● Iterează prin ea.
# ● Afișază cel mai mare număr (nu ai voie să folosești max).

print(20 * '-', 'Ex. 9', 20 * '-')
nr_mare = 0
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for numar in numere:
    if nr_mare < numar:
        nr_mare = numar
print(nr_mare)

# 10. Aceeași listă:
# ● Iterează prin ea.
# ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3
# ● Afișază noua listă.

print(20 * '-', 'Ex. 10', 20 * '-')

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = -numere[i]
print(numere)


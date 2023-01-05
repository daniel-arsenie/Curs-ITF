# Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
# Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
# X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
# X este un int.
#
# 1. Declară o listă note_muzicale în care să pui do re mi etc până la do
# ● Afișeaz-o.
# ● Inversează ordinea folosind slicing și suprascrie această listă.
# ● Printează varianta actuală (inversată).
# ● Pe această listă aplică o metodă care bănuiești că face același lucru,
# adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
# deoarece metoda face asta automat.
# ● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
# inițială.
# Concluzii: slicing e temporar, dacă vrei să păstrezi nouă variantă va trebui să
# suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face
# suprascrierea automat și permanentizează aceste modificări. Ambele variante
# își găsesc utilitatea în funcție de ce ne dorim în acel moment.
print(20 * '-', 'Exercitiul 1', 20 * '-')
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)
print('Inversare gama folosind slicing:')
note_muzicale = note_muzicale[::-1]
print(note_muzicale)
print('Inversare gama folosind reverse:')
note_muzicale.reverse()
print(note_muzicale)

# 2. De câte ori apare ‘do’?
print(20 * '-', 'Exercitiul 2', 20 * '-')
print(note_muzicale.count('do'))

# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
# Găsește 2 variante să le unești într-o singură listă.
print(20 * '-', 'Exercitiul 3', 20 * '-')
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
lista_mare = lista1 + lista2
print(lista_mare)

# 4.
# ● Sortează și afișează lista generată la exercițiul anterior.
# ● Sortează numărul 0 folosind o funcție.
# ● Afișaza iar lista.
print(20 * '-', 'Exercitiul 4', 20 * '-')
lista_mare.sort()
print(lista_mare)

# 5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
# ● Lista este goală.
# ● Lista nu este goală.
print(20 * '-', 'Exercitiul 5', 20 * '-')

if len(lista_mare) == 0:
    print('Lista este goala.')
else:
    print('Lista nu este goala.')

# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.
print(20 * '-', 'Exercitiul 6', 20 * '-')
lista_mare.clear()
print(lista_mare)

# 7. Copy paste la exercițiul 5. Verifică încă o dată.
# Acum ar trebui să se afișeze că lista e goală.

print(20 * '-', 'Exercitiul 7', 20 * '-')

if len(lista_mare) == 0:
    print('Lista este goala.')
else:
    print('Lista nu este goala.')

# 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)
print(20 * '-', 'Exercitiul 8', 20 * '-')

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())

# 9. Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie

print(20 * '-', 'Exercitiul 9', 20 * '-')
print(f'Ana a luat nota {dict1.get("Ana")}.')
print(f'Gigel a luat nota {dict1.get("Gigel")}.')
print(f'Dorel a luat nota {dict1.get("Dorel")}.')

# 10. Dorel a făcut contestație și a primit 6
# ● Modifică nota lui Dorel în 6
# ● Printează nota după modificare
print(20 * '-', 'Exercitiul 10', 20 * '-')

dict1['Gigel'] = 6
print(dict1)

# 11. Gigel se transferă din clasă
# ● Căuta o funcție care să îl șteargă
# ● Vine un coleg nou. Adaugă Ionică, cu nota 9
# ● Printează noii elevi
print(20 * '-', 'Exercitiul 11', 20 * '-')

dict1.pop('Gigel')
dict1['Ionică'] = 9
print(dict1)

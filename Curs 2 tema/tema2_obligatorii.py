# 1. Explică cu cuvintele tale în cadrul unui comentariu
# cum funcționează un if else.

print('1. Conditionalul if-else ne permite sa verificam mai multe expresii\n '
      'pentru a vedea care este adevarata si sa execute un bloc de cod\n '
      'imediat ce una dintre conditii este adevarata.')


# 2. Verifică și afișează dacă x este număr natural sau nu.
x = int(input('2. Scrie un numar intreg: \n'))

if isinstance(x, int):
    print(f'2. {x} este un numar natural.')
else:
    print(f'2. {x} este un numar real.')

# 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
if x > 0:
    print(f'3. {x} este numar pozitiv.')
elif x < 0:
    print(f'3. {x} este numar negativ.')
else:
    print(f'3. {x} este numar neutru.')


# 4. Verifică și afișează dacă x este între -2 și 13.
if x >= -2 and x <= 13:
    print(f'4. {x} este in intervalul -2 si 13.')
else:
    print(f'4. {x} nu este in intervalul -2 si 13.')

# 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
y = int(input('5. Mai scrie inca un numar intreg: \n'))

if (x - y) < 5:
    print('Diferenta este mai mica decat 5.')
else:
    print('Diferenta este mai mare decat 5.')

# 6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
if not (x <= 5 and x >= 27):
    print(f'6. {x} este in intervalul 5 si 27')
else:
    print(f'6. {x} nu este in intervalul 5 si 27')

# 7. x și y (int)
# Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai
# mare.
if x > y:
    print(f'7. {x} este mai mare decat {y}.')
elif y > x:
    print(f'7. {y} este mai mare decat {x}.')
else:
    print(f'7. {x} si {y} sunt egale')

# 8. x, y, z - laturile unui triunghi.
# Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
latura_x = int(input('8. Cat are prima latura a triunghiului?\n'))
latura_y = int(input('8. Cat are a doua latura a triunghiului??\n'))
latura_z = int(input('8. Cat are a treia latura a triunghiului??\n'))

if latura_x == latura_y == latura_z:
    print('Avem un triunghi echilateral.')
elif latura_x == latura_y or latura_x == latura_z or latura_y == latura_z:
    print('Avem un triunghi isoscel.')
else:
    print('Avem un triunghi oarecare.')

# 9. Citește o literă de la tastatură.
# Verifică și afișează dacă este vocală sau nu.

vocale = ['a', 'e', 'i', 'o', 'u']
litera =input('9. Scrie o litera:\n')

if litera in vocale:
    print('Litera este o vocala.')
else:
    print('Litera este o consoana.')

# 10.Transformă și printează notele din sistem românesc în >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F

nota = int(input('10. Ce nota ai luat?\n'))
if nota > 9:
    print('Ai luat A!')
elif nota > 8:
    print('Ai luat B!')
elif nota > 7:
    print('Ai luat C!')
elif nota > 6:
    print('Ai luat D!')
elif nota > 4:
    print('Ai luat E!')
else:
    print('Ai luat F!')

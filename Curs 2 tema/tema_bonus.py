import random
'''
11. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Ia numărul ghicit de la utilizator
Verifică și afișează dacă utilizatorul a ghicit
Vei avea 3 opțiuni
● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
● Ai ghicit. Felicitări! Ai ales x si zarul a fost y.
'''

dice_roll = random.randint(1, 6)
numar_ghicit = int(input('Alege o cifra de la 1 la 6:\n'))

if numar_ghicit < dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {numar_ghicit} dar a fost {dice_roll}.')
elif numar_ghicit > dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {numar_ghicit} dar a fost {dice_roll}.')
elif numar_ghicit == dice_roll:
    print(f'Ai ghicit. Felicitări! Ai ales {numar_ghicit} si zarul a fost {dice_roll}.')

# 1. Ne imaginăm o echipă de fotbal pt teren sintetic.
# 3 Schimbări maxime admise:
# ● Declară o Listă cu 5 jucători
# ● Schimbari_efectuate = te joci tu cu valori diferite
# ● Schimbari_max = 3

jucatori = ['jucator1', 'jucator2', 'jucator3', 'jucator4', 'jucator5']
schimbari_efectuate = 2
schimbari_max = 3
diferenta = schimbari_max - schimbari_efectuate

# Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
# - Efectuează schimbarea
# - Șterge jucătorul scos din listă
# - Adaugă jucătorul intrat
# - Afișază a intrat x, a ieșit y, mai ai z schimbări

print('Avem urmatorii jucatori in teren:')
print(jucatori)

if schimbari_efectuate < 0:  # verificam daca schimbarile efectuate sunt mai mari de 0-True
    print('Numarul de schimbari efectuate este invalid. Mai incearca.')
    exit(0)
elif schimbari_max < schimbari_efectuate:  # verificam daca schimbarile sunt mai multe decat max
    print('Ai efectuat prea multe schimbari.')
    exit(0)

jucator_inlocuit = input('Ce jucator te intereseaza sa iasa? \n')
verificare_teren = jucatori.count(jucator_inlocuit)

if verificare_teren == 1 and (schimbari_max >= schimbari_efectuate >= 0):  # jucator este pe teren - True
    schimbari_efectuate += 1
    if (schimbari_max - schimbari_efectuate) < 0:  # se poate schimba? - True
        print('Ai efectuat prea multe schimbari.')
        exit(0)
    intra = input('Cine vrei sa intre?')
    print(f'A intrat {intra}, a iesit {jucator_inlocuit}, mai ai {schimbari_max - schimbari_efectuate} schimbari.')
    jucatori.remove(jucator_inlocuit)
    jucatori.append(intra)
    print(jucatori)

# Dacă jucătorul nu e în teren:
# - Afișază ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în
# teren’
# - Afișază ‘mai ai z schimbări’
# Testează codul cu diferite valori
#
# Google search hint
# “how to check if item is în list python”

else:
    print(f'Nu se poate efectua schimbarea deoarece jucătorul {jucator_inlocuit} nu e în teren.')
    if (schimbari_max - schimbari_efectuate) < 0:
        print('Ai efectuat prea multe schimbari.')
        exit(0)
    print(f'Mai ai {schimbari_max - schimbari_efectuate} schimbari.')

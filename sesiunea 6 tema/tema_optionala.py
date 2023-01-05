# 1. Clasa Factură
# Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
# avea aceeași serie), număr, nume_produs, cantitate, pret_buc
# Constructor: toate atributele, fără serie
# Metode:
# ● schimbă_cantitatea(cantitate)
# ● schimbă_prețul(pret)
# ● schimbă_nume_produs(nume)
# # ● generează_factura() - va printa tabelar dacă reușiți
# Factura seria x număr y
# Data: generează automat data de azi
# Produs | cantitate | preț bucată | Total
# Telefon | 7 | 700 | 49000
# Indiciu pentru dată:
# https://www.geeksforgeeks.org/get-current-date-using-python/
from datetime import date
from tabulate import tabulate

today_full = date.today()
today_dmy = today_full.strftime('%d/%m/%Y')


class Factura:
    serie = 'FF'

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate_noua):
        self.cantitate = cantitate_noua
        print(f'{self.nume_produs}: Cantitatea noua: {self.cantitate}.')

    def schimba_pretul(self, pret_nou):
        self.pret_buc = pret_nou
        print(f'{self.nume_produs}: Pretul nou: {self.pret_buc} lei.')

    def schimba_nume_produs(self, nume_nou_produs):
        self.nume_produs = nume_nou_produs
        print(f'{self.nume_produs}: Numele nou al produsului: {self.nume_produs}.')

    def genereaza_factura(self):
        print(f'Factura {self.serie} numar {self.numar}\n'
              f'Data: {today_dmy}')

        total = self.cantitate * self.pret_buc
        table = [['Produs','Cantitate', 'Pret bucata', 'Total'],
                 [self.nume_produs, self.cantitate, self.pret_buc, total]]
        print(tabulate(table, tablefmt='orgtbl'))

factura1 =Factura(1,'casti JBL', 50, 120)
factura2 = Factura(18,'PS5',2, 3149)

print(20 * '-', 'Ex. 1-Exercitii optionale-schimbă_cantitatea(cantitate)', 20 * '-')
factura1.schimba_cantitatea(100)
factura2.schimba_cantitatea(4)

print(20 * '-', 'Ex. 1-Exercitii optionale-schimbă_prețul(pret)', 20 * '-')
factura1.schimba_pretul(55)
factura2.schimba_pretul(3400)

print(20 * '-', 'Ex. 1-Exercitii optionale-schimbă_nume_produs(nume)', 20 * '-')
factura1.schimba_nume_produs('Casti JBL')
factura2.schimba_nume_produs('PlayStation 5')

print(20 * '-', 'Ex. 1-Exercitii optionale-generează_factura()', 20 * '-')
factura1.genereaza_factura()
factura2.genereaza_factura()


# 2. Clasa Mașină
# Atribute: marca, model, viteza maximă, viteza_actuală, culoare, culori
# disponibile (set), înmatriculată (bool)
# Culoare = gri - toate mașinile când ies din fabrică sunt gri
# Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrică
# Culori disponibile = alege tu 5-7 culori
# Marca = alege tu - fabrica produce o singură marcă, dar mai multe modele
# Înmatriculată = False
# Constructor: model, viteza_maxima

# Metode:
# ● descrie() - se vor printa toate atributele, în afară de culori_disponibile
# ● înmatriculare() - va schimba atributul înmatriculată în True
# ● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
# culoare e în opțiunea de culori disponibile, altfel afișați o eroare
# ● accelerează(viteza) - se va accelera la o anumită viteză, dacă viteza e
# negativă-eroare, dacă viteza e mai mare decât viteza_max - masina va
# accelera până la viteza maximă
# ● franeaza() - mașina se va opri și va avea viteza 0
class ColorIsNotAvailable(Exception):
    pass
class SpeedIsNegative(Exception):
    pass

class Masina:
    marca = 'Volvo'
    viteza_actuala = 0
    culoare = 'gri'
    culori_disponibile = {'rosu', 'alb', 'negru', 'albastru', 'galben', 'verde'}
    inmatriculata = False
    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima
    def descrie(self):
        print(f'Masina marca: {self.marca}, model: {self.model}, '
              f'culoare: {self.culoare}, viteza actuala: {self.viteza_actuala}, viteza maxima: {self.viteza_maxima}, '
              f'inmatriculata: {self.inmatriculata}.')
    def inmatriculare(self):
        self.inmatriculata = True
        return self.inmatriculata
    def vopseste(self, culoare):
        if not culoare in self.culori_disponibile:
            raise ColorIsNotAvailable(f'Culoarea nu este disponibila.')
        self.culoare = culoare
        print(f'Noua culoare a masinii {self.model} este: {self.culoare}.')
    def accelereaza(self,viteza):
        if viteza < 0:
            raise SpeedIsNegative(f'Viteza aleasa are valoare negativa.')
        elif viteza > self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
            return self.viteza_actuala
        else:
            self.viteza_actuala = viteza
            return self.viteza_actuala
    def franeaza(self):
        self.viteza_actuala = 0
        return self.viteza_actuala


c1 = Masina('XC40',280)
c2 = Masina('XC60', 310)

print(20 * '-', 'Ex. 2-Exercitii optionale-descrie()', 20 * '-')
c1.descrie()
c2.descrie()

print(20 * '-', 'Ex. 2-Exercitii optionale-inmatriculare()', 20 * '-')
print(c1.inmatriculare())
print(c2.inmatriculare())

print(20 * '-', 'Ex. 2-Exercitii optionale-vopseste(culoare)', 20 * '-')
c1.vopseste('alb')
# c2.vopseste('mov') # linia comentata arunca eroare
c2.vopseste('negru')


print(20 * '-', 'Ex. 2-Exercitii optionale-viteza', 20 * '-')
print(c1.accelereaza(150))
print(c2.accelereaza(270))

print(20 * '-', 'Ex. 2-Exercitii optionale-viteza', 20 * '-')
print(c1.franeaza())
print(c2.franeaza())

print(20 * '-', 'Ex. 2-Exercitii optionale-descriere finala', 20 * '-')

c1.descrie()
c2.descrie()

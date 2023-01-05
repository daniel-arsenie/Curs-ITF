# 1.Clasa Cerc
# Atribute: rază, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()

class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f'Cerul este de culoare {self.culoare} iar raza este {self.raza}.')

    def aria(self):
        arie_cerc = (self.raza ** 2) * 3.1416
        return arie_cerc

    def diametru(self):
        diametru_cerc = 2 * self.raza
        return diametru_cerc

    def circumferinta(self):
        return self.diametru() * 3.1416


c1 = Cerc(13, 'albastru')
c2 = Cerc(10, 'roz')

print(20 * '-', 'Ex. 1 descriere cerc', 20 * '-')
c1.descrie_cerc()
c2.descrie_cerc()

print(20 * '-', 'Ex. 1 aria()', 20 * '-')
print(c1.aria())
print(c2.aria())


print(20 * '-', 'Ex. 1 diametru()', 20 * '-')
print(c1.diametru())
print(c2.diametru())


print(20 * '-', 'Ex. 1 circumferinta()', 20 * '-')
print(c1.circumferinta())
print(c2.circumferinta())

# 2. Clasa Dreptunghi
# Atribute: lungime, lățime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
# self.culoare. Poți verifica schimbarea culorii prin apelarea metodei
# descrie().

class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f'Dreptunghiul are lungimea {self.lungime}, '
              f'latimea {self.latime}, '
              f'culoarea {self.culoare}.')

    def aria(self):
        aria_dreptunghi = self.latime * self.lungime
        return aria_dreptunghi

    def perimetrul(self):
        perimetru = 2 * (self.aria())
        return perimetru

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare

d1 = Dreptunghi(7,3, 'roz')
d2 = Dreptunghi(10,5,'albastru')

print(20 * '-', 'Ex. 2 descrie()', 20 * '-')
d1.descrie()
d2.descrie()

print(20 * '-', 'Ex. 2 aria()', 20 * '-')
print(d1.aria())
print(d2.aria())

print(20 * '-', 'Ex. 2 perimetrul()', 20 * '-')
print(d1.perimetrul())
print(d2.perimetrul())

print(20 * '-', 'Ex. 2 shimba culoarea()', 20 * '-')
d1.schimba_culoarea('galben')
d1.descrie()

d2.schimba_culoarea('alb')
d2.descrie()


# 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)

class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.procent = None
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu
    def descrie(self):
        print(f'Nume: {self.nume}, prenume: {self.prenume}, salariu: RON {self.salariu}.')
    def nume_complet(self):
        return f'{self.nume} {self.prenume}'
    def salariu_lunar(self):
        return self.salariu
    def salariu_anual(self):
        return 12 * self.salariu
    def marire_salariu(self, procent):
        self.procent =  procent
        return self.salariu * ((100 + self.procent) / 100)

angajat1 = Angajat('Oprea', 'Daniel', 1000)
angajat2 = Angajat('Vasiliev', 'Aleksei', 2500)

print(20 * '-', 'Ex. 3 descrie()', 20 * '-')
angajat1.descrie()
angajat2.descrie()

print(20 * '-', 'Ex. 3 nume_complet()', 20 * '-')
print(angajat1.nume_complet())
print(angajat2.nume_complet())

print(20 * '-', 'Ex. 3 salariu_lunar()', 20 * '-')
print(angajat1.salariu_lunar())
print(angajat2.salariu_lunar())

print(20 * '-', 'Ex. 3 salariu_anual()', 20 * '-')
print(angajat1.salariu_anual())
print(angajat2.salariu_anual())

print(20 * '-', 'Ex. 3 marire_salariu(procent)', 20 * '-')
print(angajat1.marire_salariu(20))
print(angajat2.marire_salariu(50))


# 4. Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)

class Cont:
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold
    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei.')
    def debitare_cont(self, suma):
        self.sold += suma
        print(f'{self.titular_cont}: Am adaugat cu succes {suma} lei. Soldul actual: {self.sold} lei.')
    def creditare_cont(self, suma):
        if suma > self.sold:
            print(f'{self.titular_cont}: Nu se poate face plata. Fonduri insuficiente.')
        else:
            self.sold -= suma
            print(f'{self.titular_cont}: Ati platit {suma} lei. Soldul actual: {self.sold} lei.')

cont1 = Cont('GB29 NWBK 6016 1331 9268 19', 'Oprea Daniel', 4000)
cont2 = Cont('AT48 3200 0000 1234 5864', 'Vasiliev Aleksei', 12500)

print(20 * '-', 'Ex. 4-afisare_sold()', 20 * '-')
cont1.afisare_sold()
cont2.afisare_sold()

print(20 * '-', 'Ex. 4-debitare_cont(suma)', 20 * '-')
cont1.debitare_cont(1000)
cont2.debitare_cont(1000)

print(20 * '-', 'Ex. 4-debitare_cont(suma)', 20 * '-')
cont1.creditare_cont(1500)
cont1.creditare_cont(1500)
cont1.creditare_cont(1500)
cont1.creditare_cont(1500)

cont2.creditare_cont(1500)
cont2.creditare_cont(3000)
cont2.creditare_cont(9100)

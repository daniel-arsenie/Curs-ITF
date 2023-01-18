# 1. Alegeti 3 functii din cele implementate la tema anterior
# si scrieti unit tests pentru ele folosind unittest.

def get_sum_of_2_numbers(a, b):
    result = a + b
    return result


def area_of_rectangle(length, width):
    area = length * width
    return area


def if_char_in_specified_string(n, lst):
    return True if n in lst else False


# 2. Alegeti 2 clase din cele implementate la tema anterior
# si scrieti unit teste pentru toate metodele folosind unittest.

class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f'Cerul este de culoare {self.culoare} iar raza este {self.raza}.')

    def aria_cerc(self):
        aria_cerc = self.raza ** 2
        return aria_cerc

    def diametru_cerc(self):
        diametru_cerc = 2 * self.raza
        return diametru_cerc

    def circumferinta_cerc(self):
        return self.diametru_cerc() * 3.1416


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

# 3. Alegeti una din temele de mai sus
# si convertiti testele din unittest in pytest

# Folosind TDD, rezolvati urmatoarea problema:
# Sa se scrie o ierarhie de clase pentru forme geometrice: FormaGeometrica, Patrat, Dreptunghi, Cerc.
# FormaGeometrica este interfata, adice clasa abstracta cu doar metode astracte.
# Metode: arie(), perimetru(). Sa se mosteneasca interfata, si sa se implementeze cele 2 metode
# pentru fiecare din cele 3 forme geometrice.

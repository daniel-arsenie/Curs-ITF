# De raspuns la intrebarile:
# 1. Ce inseamna if __name__ == "__main__" scris intr - un fisier python?
# Raspuns: pastreaza o bucata de cod pentru a fi rulat
# doar atunci cand programul este rulat ca script

# 2. Cum instalam un pachet extern python?
# Raspuns:mergem in bara de jos in Pycharm la Python Packages,
# cautam packetul care ne itereseaza(ex: Selenium)
# si click pe Install Package de langa Version


# 3. Ce este dataclass in python?
# Raspuns: "dataclass" este un modul care poate fi importat
# pentru a genera "metode speciale"(__init__() si __repr__())
# intr-o clasa definita de noi.


# 4. Ce este functia hash?
# Raspuns: "hash" este o functie in Python care returneaza valoarea unui obiect.
# hash are ca valoare de baza un integer.
# Obiectele schimbate folosind hash() nu ma pot reveni la valoarea de dinainte de hash().
# int_val = 4      -> hash(int_val) va fi tot 4
# flt_val = 24.56  -> hash(flt_val) va fi 1291272085159665688


# 5. Cum pot face codul de mai jos sa functioneze corect?

# class Person:
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name
#
#     def __eq__(self, other):
#         return isinstance(other, Person) and self.age == other.age and self.name == other.name
#
#
# s = set()
# p = Person(29, "Adrian")
# s.add(p)

class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    # __eq__ folosim doar daca vrem sa comparam 2 obiecte
    # def __eq__(self, other):
    #     return isinstance(other, Person) and self.age == other.age and self.name == other.name

    def __str__(self):  # str- creem un string atunci cand creem un obiect si dam print la obiect
        return f'Person: {self.name}, Age: {self.age}'

    def __repr__(self):  # folosit pentru printarea colectiilor de obiecte, liste
        # ca sa facem lista din obiectele noastre
        return str(self)


p = Person(29, "Adrian")
# p2 = Person(18, 'Stefan')

s = set()
s.add(p)
# s.add(p2)

print(s)

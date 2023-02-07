"""Design pattern - Adaptor (Structural)"""


# ToDo: create a Class for each attribute and a "say_hi" method,
#  that calls the function specific to each individual.


class Elf:
    def say_hi_in_elven(self):
        print('Elf says: Hello from our lands!')


class Dwarf:
    def say_hi_in_dwarven(self):
        print('Dwarf says: Hello from our lands!')


class Human:
    def say_hi_in_human(self):
        print('Human says: Hello from our lands!')


minions = [Elf(), Dwarf(), Human()]

for minion in minions:
    if isinstance(minion, Elf):
        minion.say_hi_in_elven()
    elif isinstance(minion, Dwarf):
        minion.say_hi_in_dwarven()
    else:
        minion.say_hi_in_human()

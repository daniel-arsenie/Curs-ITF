# Creational Patterns
# Factory Pattern
"""
a.

The factory pattern comes under the creational patterns list category.
 It provides one of the best ways to create an object.
 In factory pattern, objects are created without exposing the logic
 to client and referring to the newly created object using a common interface.

b.
PRO:
    You avoid tight coupling between the creator and the concrete products.
CON:
    The code may become more complicated since you need to introduce
     a lot of new subclasses to implement the pattern. 
     The best case scenario is when you’re introducing the pattern 
     into an existing hierarchy of creator classes.
"""


class Button(object):
    html = ""

    def get_html(self):
        return self.html


class Image(Button):
    html = "<img></img>"


class Input(Button):
    html = "<input></input>"


class Flash(Button):
    html = "<obj></obj>"


class ButtonFactory():
    def create_button(self, typ):
        targetclass = typ.capitalize()
        return globals()[targetclass]()


button_obj = ButtonFactory()
button = ['image', 'input', 'flash']
for b in button:
    print(button_obj.create_button(b).get_html())
"""
d. 

If we start by defining a class called TransportationByTrucks, and
 use this class for our transportation app then when we want to implement another type of transportation
 we should check this class and find a way to add one. But what if we want to add 20?
 But if we have a parent class Logistics that has a 'create_transport' function in it, and then in
 any child Class we can overwrite this function and build any type of transportation
 (sea, land, bike, underground, rail etc.).
"""

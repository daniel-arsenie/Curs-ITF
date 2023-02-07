# Behavioral Patterns
# Mediator
"""
a.
    Mediator pattern is used to reduce communication complexity between multiple objects or classes.
    This pattern provides a mediator class which normally handles all the communications
    between different classes and supports easy maintenance of the code by loose coupling.

b. PROS:
    It decouples the component classes.
        A component only depends on the mediator.
        It makes a many-to-many interaction a one-to-many interaction.
   CONS:
    The mediator implementation is heavy.
        It would seem to know a lot of things.
        If not careful, it can become a God object(sometimes also called an omniscient or all-knowing object)
            is an object that references a large number of distinct types,
            has too many unrelated or uncategorized methods, or some combination of both.


"""
# c.

from abc import ABC, abstractmethod


class User_1(ABC):
    def __init__(self, med, name_):
        self.mediator = med
        self.name = name_

    @abstractmethod
    def send(self, msg):
        pass

    @abstractmethod
    def receive(self, msg):
        pass


class Chat_Mediator:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, msg, user):
        for u in self.users:
            if u != user:
                u.receive(msg)


class User_1(User_1):
    def send(self, msg):
        print(self.name + ": we are providing information : " + msg)
        self.mediator.send_message(msg, self)

    def receive(self, msg):
        print(self.name + ": Received Message from Ms sweta: " + msg)


if __name__ == '__main__':
    mediator_1 = Chat_Mediator()
    consumer1 = User_1(mediator_1, "Sweta")
    consumer2 = User_1(mediator_1, "Aditya")
    consumer3 = User_1(mediator_1, "Rakhi")
    consumer4 = User_1(mediator_1, "Mishri")
    mediator_1.add_user(consumer1)
    mediator_1.add_user(consumer2)
    mediator_1.add_user(consumer3)
    mediator_1.add_user(consumer4)
    consumer1.send("Hello, every one is invited and we feel immense pleasure to accompanied by you .")

"""
d. real-life use:
    the most common example is the one with the control tower of an airport.
    Basically we have some objects that need to communicate to eachother but
    to do this it would require a lot of knowledge for both sides. This entire hassle
    cand have a simple solution: the Control Tower that can manage all dependencies, 
    has a lot of information about the objects and can control the output.
"""

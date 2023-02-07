# Structural Patterns
# Adapter
"""
a.
    This pattern involves a single class, which is responsible to join
    functionalities of independent or incompatible interfaces.
    A real life example could be the case of a card reader, which
    acts as an adapter between memory card and a laptop.
    You plug in the memory card into the card reader and
    the card reader into the laptop so that memory card can be read via the laptop.

b.
PRO:
    Single Responsibility Principle.
     You can separate the interface or data conversion code from the primary business logic of the program.
    Open/Closed Principle. You can introduce new types of adapters into the program
      without breaking the existing client code, as long as they work with the adapters through the client interface.
CON:
    The overall complexity of the code increases because you need to introduce
     a set of new interfaces and classes. Sometimes it’s simpler just to change
     the service class so that it matches the rest of your code.
"""


# c.

# Adaptee (source) interface
class EuropeanSocketInterface:
    def voltage(self): pass

    def live(self): pass

    def neutral(self): pass

    def earth(self): pass


# Adaptee
class Socket(EuropeanSocketInterface):
    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1

    def earth(self):
        return 0


# Target interface
class USASocketInterface:
    def voltage(self): pass

    def live(self): pass

    def neutral(self): pass


# The Adapter
class Adapter(USASocketInterface):
    __socket = None

    def __init__(self, socket):
        self.__socket = socket

    def voltage(self):
        return 110

    def live(self):
        return self.__socket.live()

    def neutral(self):
        return self.__socket.neutral()


# Client
class ElectricKettle:
    __power = None

    def __init__(self, power):
        self.__power = power

    def boil(self):
        if self.__power.voltage() > 110:
            print("Kettle on fire!")
        else:
            if self.__power.live() == 1 and \
                    self.__power.neutral() == -1:
                print("Coffee time!")
            else:
                print("No power.")


def main():
    # Plug in
    socket = Socket()
    adapter = Adapter(socket)
    kettle = ElectricKettle(adapter)

    # Make coffee
    kettle.boil()

    return 0


main()

"""
d. real-life usage
Let's say a bank client has an account in GBP
but he has a pending RON payment. He does not know what amount og GBP 
he should exchange. For this reason, the client wants to have a function
that can show him in real time his balance in different currencies. We have to use an adapter
that can convert automatically the current balance into another currency using updated exchange rates.
"""

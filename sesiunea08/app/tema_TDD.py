from abc import abstractmethod, ABC
from dataclasses import dataclass


class FormaGeometrica(ABC):
    @abstractmethod
    def arie(self):
        pass

    @abstractmethod
    def perimetru(self):
        pass


@dataclass
class Patrat(FormaGeometrica):
    latura: int

    def arie(self):
        return self.latura ** 2

    def perimetru(self):
        return 4 * self.latura


@dataclass()
class Dreptunghi(FormaGeometrica):
    lungime: int
    latime: int

    def arie(self):
        return self.lungime * self.latime

    def perimetru(self):
        return 2 * (self.latime + self.lungime)


@dataclass()
class Cerc(FormaGeometrica):
    pi = 3.14
    r: int

    def arie(self):
        return self.pi * (self.r ** 2)

    def perimetru(self):
        return 2 * self.pi * self.r

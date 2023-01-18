# Folosind TDD, rezolvati urmatoarea problema:
# Sa se scrie o ierarhie de clase pentru forme geometrice: FormaGeometrica, Patrat, Dreptunghi, Cerc.
# FormaGeometrica este interfata, adice clasa abstracta cu doar metode astracte.
# Metode: arie(), perimetru().
# Sa se mosteneasca interfata, si sa se implementeze cele 2 metode
# pentru fiecare din cele 3 forme geometrice.

import pytest
from Teme.sesiunea8.app.tema_TDD import Patrat, Dreptunghi, Cerc


@pytest.mark.parametrize('n, expected', [
    (Patrat(10), 100),
    (Dreptunghi(10, 20), 200),
    (Cerc(10), 314)
])
def test_arie(n, expected):
    assert n.arie() == expected


@pytest.mark.parametrize('n, expected', [
    (Patrat(10), 40),
    (Dreptunghi(10, 20), 60),
    (Cerc(10), 62.800000000000004)
])
def test_perimetru(n, expected):
    assert n.perimetru() == expected

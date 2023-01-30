import unittest
from parameterized import parameterized

from Teme.sesiunea8.app.tema_testare import get_sum_of_2_numbers, area_of_rectangle, if_char_in_specified_string
from Teme.sesiunea8.app.tema_testare import Cerc, Dreptunghi


class TestTemaTestare(unittest.TestCase):
    def setUp(self):
        self.c1 = Cerc(10, 'gri')
        self.d1 = Dreptunghi(10, 20, 'mov')

    @parameterized.expand([
        (2, 3, 5),
        (8, 12, 20),
        (12, 10, 22)
    ])
    def test_get_sum_of_2_numbers(self, n1, n2, expected):
        self.assertEqual(get_sum_of_2_numbers(n1, n2), expected)

    @parameterized.expand([
        (10, 5, 50),
        (11, 12, 132),
        (1, 12, 12)
    ])
    def test_area_of_rectangle(self, length, wid, expected):
        self.assertEqual(area_of_rectangle(length, wid), expected)

    @parameterized.expand([
        ('a', 'Ana are mere', True),
        ('x', 'Ana are mere', False),
        ('', 'Ana are mere', True),
        (' ', 'Anaaremere', False)
    ])
    def test_if_char_in_specified_string(self, n, lst, expected):
        self.assertEqual(if_char_in_specified_string(n, lst), expected)

    def test_aria_cerc(self):
        self.assertEqual(self.c1.aria_cerc(), 100)

    def test_diametru_cerc(self):
        self.assertEqual(self.c1.diametru_cerc(), 20)

    def test_circumferinta_cerc(self):
        self.assertEqual(self.c1.circumferinta_cerc(), 62.832)

    def test_aria_dreptunghi(self):
        self.assertEqual(self.d1.aria_dreptunghi(), 200)

    def test_perimetru_dreptunghi(self):
        self.assertEqual(self.d1.perimetru_dreptunghi(), 400)

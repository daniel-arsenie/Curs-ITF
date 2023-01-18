import unittest
from parameterized import parameterized

from Teme.sesiunea8.app.tema_testare import get_sum_of_2_numbers, area_of_rectangle, if_char_in_specified_string


class TestTemaTestare(unittest.TestCase):
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
    def test_area_of_rectangle(self, len, wid, expected):
        self.assertEqual(area_of_rectangle(len, wid), expected)

    @parameterized.expand([
        ('a', 'Ana are mere', True),
        ('x', 'Ana are mere', False),
        ('', 'Ana are mere', True),
        (' ', 'Anaaremere', False)
    ])
    def test_if_char_in_specified_string(self, n, lst, expected):
        self.assertEqual(if_char_in_specified_string(n, lst), expected)

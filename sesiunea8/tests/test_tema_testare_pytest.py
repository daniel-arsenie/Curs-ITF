import pytest
from Teme.sesiunea8.app.tema_testare import Cerc, Dreptunghi


@pytest.mark.parametrize('n, expected', [
    (10, 100),
    (11, 121)
])
def test_aria_cerc(n, expected):
    c1 = Cerc(n, 'roz')
    assert c1.aria_cerc() == expected


@pytest.mark.parametrize('n, expected', [
    (10, 20),
    (11, 22)
])
def test_diametru_cerc(n, expected):
    c1 = Cerc(n, 'roz')
    assert c1.diametru_cerc() == expected


@pytest.mark.parametrize('n, expected', [
    (10, 62.832),
    (11, 69.1152)
])
def test_circumferinta_cerc(n, expected):
    c1 = Cerc(n, 'roz')
    assert c1.circumferinta_cerc() == expected


@pytest.mark.parametrize('lun, lat, expected', [
    (10, 5, 50),
    (11, 12, 132)
])
def test_aria(lun, lat, expected):
    d1 = Dreptunghi(lun, lat, 'mov')
    assert d1.aria() == expected


@pytest.mark.parametrize('lun, lat, expected', [
    (10, 5, 100),
    (11, 12, 264)
])
def test_perimetru(lun, lat, expected):
    d1 = Dreptunghi(lun, lat, 'albastru')
    assert d1.perimetrul() == expected

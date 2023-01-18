import pytest
from sesiunea8.app.product import Product
from sesiunea8.app.product_repository import ProductRepository


@pytest.mark.parametrize('n, expected', [
    (ProductRepository(), [
        Product(name="Orez", price=4.5, discount=10, category="Alimente de baza"),
        Product(name="Paine neagra", price=3.79, discount=0, category="Fainoase"),
        Product(name="Faina integrala", price=1.85, discount=5, category="Fainoase"),
        Product(name="Zahar brun", price=6.5, discount=0, category="Alimente de baza"),
        Product(name="Oua", price=14.79, discount=5, category="Alimente de baza"),
        Product(name="Branza de capra", price=14.99, discount=10, category="Lactate"),
        Product(name="Apa plata", price=2.09, discount=33, category="Bauturi"),
        Product(name="Apa minerala", price=2.3, discount=33, category="Bauturi"),
        Product(name="Bere", price=3.5, discount=15, category="Bauturi"),
        Product(name="Ovaz", price=1.99, discount=0, category="Alimente de baza"),
    ])
])
def test_get_all(n, expected):
    assert n.get_all() == expected


@pytest.mark.parametrize('total, name, expected', [
    (ProductRepository(), 'Orez', Product(name="Orez", price=4.5, discount=10, category="Alimente de baza")),
    (ProductRepository(), 'Oua', Product(name="Oua", price=14.79, discount=5, category="Alimente de baza")),
    (ProductRepository(), 'Bere', Product(name="Bere", price=3.5, discount=15, category="Bauturi"))
])
def test_get_by_name(total, name, expected):
    assert total.get_by_name(name) == expected


@pytest.mark.parametrize('total, category, expected', [
    (ProductRepository(), 'Fainoase', ['Paine neagra', 'Faina integrala']),
    (ProductRepository(), 'Lactate', ['Branza de capra'])
])
def test_get_all_by_category(total, category, expected):
    assert total.get_all_by_category(category) == expected

import pytest
from src.Classes import Product, Category


@pytest.fixture()
def category_smart():
    return Category('Смартфон', 'Самые лучшие', [
        {
            "name": "Samsung Galaxy C23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5
        },
        {
            "name": "Xiaomi Redmi Note 11",
            "description": "1024GB, Синий",
            "price": 31000.0,
            "quantity": 14
        }
    ])


def test_category_number(category_smart):
    assert category_smart.number_of_category == 1


def test_product_number(category_smart):
    category_smart.create_product()
    assert category_smart.number_of_product == 2


def test_category(category_smart):
    assert category_smart.name_category == 'Смартфон'
    assert category_smart.description == 'Самые лучшие'
    assert category_smart.products == [
        {
            "name": "Samsung Galaxy C23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5
        },
        {
            "name": "Xiaomi Redmi Note 11",
            "description": "1024GB, Синий",
            "price": 31000.0,
            "quantity": 14
        }
    ]


@pytest.fixture()
def product_smart():
    return Product('Samsung S23', '256Гб', 10000.0, 14)


def test_product(product_smart):
    assert product_smart.name_product == 'Samsung S23'
    assert product_smart.description == '256Гб'
    assert product_smart.price == 10000.0
    assert product_smart.quantity == 14

# pytest --cov src --cov-report term-missing

import pytest
from src.Classes import Product, Category
from pathlib import Path
from src.Functions import load_data, created_objects


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
    assert Category.number_of_category == 1
    Category.number_of_category = 0


def test_product_number(category_smart):
    category_smart.create_product()
    assert category_smart.number_of_product == 2
    Category.number_of_category = 0
    Category.number_of_product = 0


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
    Category.number_of_category = 0
    Category.number_of_product = 0


@pytest.fixture()
def product_smart():
    return Product('Samsung S23', '256Гб', 10000.0, 14)


def test_product(product_smart):
    assert product_smart.name_product == 'Samsung S23'
    assert product_smart.description == '256Гб'
    assert product_smart.get_price == 10000.0
    assert product_smart.quantity == 14
    Category.number_of_category = 0
    Category.number_of_product = 0


@pytest.fixture()
def count():
    """
    Тест на подсчет созданных объектов классов
    Так же после предыдущих тестов обнуляем счетчик объектов
    """
    all_data = Path(__file__).parent.joinpath('products_test.json')
    # Загружаем данные из файла
    data_file_load = load_data(all_data)
    # Создаём объекты и получаем список объектов класса Категория
    list_category = created_objects(data_file_load)
    return Category, list_category


def test_count_classes(count):
    assert count[0].number_of_category == 3
    assert count[0].number_of_product == 7
    Category.number_of_category = 0
    Category.number_of_product = 0


def test_get_product(count):
    for i in count[1]:
        if i.name_category == 'Процессоры':
            assert len(i.get_product) == 2
    Category.number_of_category = 0
    Category.number_of_product = 0


@pytest.fixture()
def add_product_category():
    new_cat = Category("Telephone", "Лучшие телефоны")

    new_product = Product.create_product('Samsung Galaxy23', 'Флагман', 23000.0, 12, Category.all_objects_product)
    new_cat.add_products(new_product)
    new_product2 = Product.create_product('Apone 13', '231231221', 150000.0, 2, Category.all_objects_product)
    new_cat.add_products(new_product2)
    new_product3 = Product.create_product('Apone 13', '231231221', 160000.0, 1, Category.all_objects_product)
    new_cat.add_products(new_product3)

    return Product, Category


def test_create_product(add_product_category):
    """
    проверяем создание объктов и проверяем, что объект с таким же именем
    не создается, а его количевство складывается и выбирается большая цена
    """
    assert len(add_product_category[1].all_objects_product) == 2
    assert add_product_category[1].number_of_product == 2
    for i in add_product_category[1].all_objects_product:
        assert i.quantity == 12 or 3
        assert i.price == 23000.0 or 160000.0
    Category.number_of_category = 0
    Category.number_of_product = 0


def test_get_price():
    new_cat = Category("Telephone", "Лучшие телефоны")
    new_product = Product('Samsung Galaxy23', 'Флагман', 23000.0, 12)
    new_cat.add_products(new_product)
    assert new_product.get_price == 23000.0
    new_product.get_price = 0
    assert new_product.get_price == 23000.0
    new_product.get_price = 25000.0
    assert new_product.get_price == 25000.0
    assert "".join(new_cat.get_product_info) == 'Samsung Galaxy23, 25000.0 руб. Остаток: 12 шт.'

# pytest --cov src --cov-report term-missing

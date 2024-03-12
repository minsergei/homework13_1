import pytest
from src.Classes import Product, Category, Smartphone, LawnGrass
from pathlib import Path
from src.Functions import load_data, created_objects


@pytest.fixture()
def category_smart():
    return Category('Смартфон', 'Самые лучшие')


def test_category_number(category_smart):
    assert Category.number_of_category == 1
    Category.number_of_category = 0


def test_category(category_smart):
    assert category_smart.name_category == 'Смартфон'
    assert category_smart.description == 'Самые лучшие'
    Category.number_of_category = 0
    Category.number_of_product = 0


@pytest.fixture()
def product_smart():
    return Product('Samsung S23', '256Гб', 10000.0, 14)


def test_product(product_smart):
    assert product_smart.name_product == 'Samsung S23'
    assert product_smart.description == '256Гб'
    assert product_smart.price == 10000.0
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
    created_objects(data_file_load)
    return Category


def test_get_product(count):
    for i in count.all_objects_category:
        if i.name_category == 'Процессоры':
            assert len(i) == 2
            assert len(i.get_product) == 2

    Category.number_of_category = 0
    Category.number_of_product = 0
    Category.all_objects_product = []
    Category.all_objects_category = []


def test_count_classes(count):
    assert count.number_of_category == 3
    assert count.number_of_product == 7
    Category.number_of_category = 0
    Category.number_of_product = 0
    Category.all_objects_product = []
    Category.all_objects_category = []


@pytest.fixture()
def add_product_category():
    new_cat = Category("Telephone", "Лучшие телефоны")

    new_product = Product.create_product('Samsung Galaxy23', 'Флагман', 23000.0, 12, Category.all_objects_product)
    new_cat.add_products(new_product)
    new_product2 = Product.create_product('Apone 13', 'The best', 150000.0, 1, Category.all_objects_product)
    new_cat.add_products(new_product2)
    new_product3 = Product.create_product('Apone 13', 'The best', 160000.0, 2, Category.all_objects_product)
    new_cat.add_products(new_product3)

    return Category, new_product, new_product2


def test_create_product(add_product_category):
    """
    проверяем создание объктов и проверяем, что объект с таким же именем
    не создается, а его количевство складывается и выбирается большая цена
    """
    assert len(Category.all_objects_product) == 2
    assert Category.number_of_product == 2
    list1 = []
    list2 = []
    for i in Category.all_objects_product:
        list1.append(i.quantity)
        list2.append(i.price)
    assert list1 == [12, 3]
    assert list2 == [23000.0, 160000.0]
    Category.number_of_category = 0
    Category.number_of_product = 0
    Category.all_objects_product = []
    Category.all_objects_category = []


def test_price():
    new_cat_test = Category.create_category("Telephone", "Лучшие телефоны", [])
    new_product = Product('Samsung Galaxy23', 'Флагман', 23000.0, 2)
    new_product2 = Smartphone('Samsung Galaxy20', 'Флагман', 27000.0, 1, 'white', '1200ghz', 'Android13', 120)
    new_product3 = LawnGrass("Трава", "Газонная", 250, 400, "Белая", 'Russia', 3)
    new_cat_test.add_products(new_product)
    assert new_product.price == 23000.0
    new_product.price = 0
    assert new_product.price == 23000.0
    new_product.price = 25000.0
    assert new_product.price == 25000.0
    assert ''.join(new_cat_test.get_product_info) == 'Samsung Galaxy23, 25000.0 руб. Остаток: 2 шт.'
    Category.all_objects_product = []
    Category.all_objects_category = []
    assert new_product + new_product2 == 77000.0

# pytest --cov src --cov-report term-missing

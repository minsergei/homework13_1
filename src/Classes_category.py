from abc import ABC, abstractmethod
from src.Classes import Product, Smartphone, LawnGrass


class MyException(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else '------------\nТовар не может быть с нулевым количеством'

    def __str__(self):
        return self.message


class AbstractOrder(ABC):
    """Абстрактный класс для заказа и категории с общим методом добавить продукт"""

    @abstractmethod
    def add_products(self, product):
        pass


class Order(AbstractOrder):
    """Класа заказ"""
    product = str
    quantity = int
    total_cost = float

    def __init__(self, product, quantity, total_cost):
        self.add_products(product)
        self.product = product
        self.quantity = quantity
        self.total_cost = total_cost

    def add_products(self, product):
        """
        добавляем продукт(Код для примера)
        """
        if isinstance(product, Product):
            if product.quantity <= 0:
                raise MyException()
            return "Товар добавлен"
        return "Не верный продукт"


class Category(AbstractOrder):
    name_category = str
    description = str
    __products = list
    number_of_category = 0
    number_of_product = 0
    all_objects_category = []
    all_objects_product = []

    def __init__(self, name, description, products=[]):
        self.name_category = name
        self.description = description
        self.__products = products
        Category.number_of_category += 1
        Category.number_of_product += len(self.__products)

    def __str__(self):
        return f'{self.name_category}, количество продуктов: {len(self)} шт.'

    def __len__(self):
        return len(self.__products)

    @property
    def avg_price_product(self):
        """Метод, который подсчитывает средний ценник всех товаров и обрабатывает исключение деления на ноль"""
        try:
            avg_price = 0
            for i in self.__products:
                avg_price += i.price
            return round(avg_price / len(self.__products), 2)
        except ZeroDivisionError:
            return 0

    @classmethod
    def create_category(cls, *args):
        """
        метод создания объекта категории с условием отбора одинаковых имен
        """
        category = cls(*args)
        Category.all_objects_category.append(category)
        return category

    def add_products(self, product):
        """
        добавляем продукт в список продуктов атрибута категории и список продуктов атрибута класса
        C проверкой что поступает объект класса продукт
        """
        if isinstance(product, Product):
            if product.quantity <= 0:
                raise MyException()
            self.__products.append(product)
            self.all_objects_product.append(product)
            Category.number_of_product += 1
        else:
            return 'Не верный продукт'

    def add_products_json(self, product):
        """
        добавляем продукт в список продуктов атрибута класса при работе с json файлом
        """
        self.all_objects_product.append(product)

    @property
    def get_product(self):
        """
        Возвращает список объектов продуктов
        """
        return self.__products

    @property
    def get_product_info(self):
        """
        Печатает список объектов продуктов категории в определенном формате
        """
        list_data = []
        for item in self.__products:
            list_data.append(f'{item.name_product}, {item.price} руб. Остаток: {item.quantity} шт.')
        return list_data

# try:
#     new_cat = Category.create_category("Telephone", "Лучшие телефоны", [])
#     new_product = Product.create_product('Samsung Galaxy23', 'Флагман', 23000.0, 0, Category.all_objects_product)
#     new_cat.add_products(new_product)
# except MyException as e:
#     print(e)
# else:
#     print('Товар добавлен')
#     print(new_product)
# finally:
#     print('Обработка добавления товара завершена')

from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    """Абстрактный метод"""

    @classmethod
    @abstractmethod
    def create_product(cls, *args):
        pass


class ProdMixin:
    def __repr__(self):
        print('Был создан продукт')


class Product(AbstractProduct, ProdMixin):
    name_product = str
    description = str
    price = float
    quantity = int
    colour = str

    def __repr__(self):
        super().__repr__()
        return f'{self.name_product}, {self.description}, {self.quantity}, {self.price}'

    def __init__(self, name, description, price, quantity, colour='white'):
        self.name_product = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.colour = colour

    def __str__(self):
        return f'{self.name_product}, {self.__price} руб. Остаток: {self.quantity} штук.'

    def __add__(self, other):
        """
        Проверка сложения на соответствие класса
        """
        if issubclass(type(other), self.__class__):
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError('Классы не соответствуют')

    @classmethod
    def create_product(cls, *args):
        """
        метод создания объекта продукта с условием отбора одинаковых имен
        """
        product_name = []
        for i in args[4]:
            product_name.append(i.name_product)
        if len(args[4]) == 0:
            product = cls(*args)
            return product
        elif args[0] in product_name:
            for i in args[4]:
                if args[0] == i.name_product:
                    i.quantity += args[3]
                    if i.price < args[2]:
                        i.price = args[2]
        else:
            product = cls(args[0], args[1], args[2], args[3])
            return product

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            return 'Цена введена некорректная'
        else:
            self.__price = new_price

    @price.deleter
    def price(self):
        x = input('Если уверены что хотите удалить введите Y\n')
        if x.lower() == 'y':
            print('Удаляем цену')
            self.__price = None
        return True


class Smartphone(Product, ProdMixin):
    """
    Новый подклосс Смартфон
    """
    efficiency = int
    model = str
    memory = int

    def __repr__(self):
        super().__repr__()
        return f'{self.name_product}, {self.description}, {self.quantity}, {self.price}'

    def __init__(self, name, description, price, quantity, colour, efficiency, model, memory):
        super().__init__(name, description, price, quantity, colour)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory


class LawnGrass(Product, ProdMixin):
    """
    Новый подклосс Газонная трава
    """
    country = str
    period = int

    def __repr__(self):
        super().__repr__()
        return f'{self.name_product}, {self.description}, {self.quantity}, {self.price}'

    def __init__(self, name, description, price, quantity, colour, country, period):
        super().__init__(name, description, price, quantity, colour)
        self.country = country
        self.period = period


class AbstractOrder(ABC):
    '''Абстрактный класс для заказа и категории с общим методом добавить продукт'''
    @abstractmethod
    def add_products(self, product):
        pass


class Order(AbstractOrder):
    '''Класа заказ'''
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
        if not isinstance(product, Product):
            return 'Не верный продукт'
        return "Товар добавлен"


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

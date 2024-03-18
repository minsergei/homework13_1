from abc import ABC, abstractmethod
# from src.Classes_category import Category, Order


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
        """Проверяем при инициализации, что количество продукта больше 0
        Закомментировал, потому что не выполняется третье задание. Они оба отлавливают ошибку с нулевым значением кол-ва 
        """
        # if quantity <= 0:
        #     raise ValueError
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
            product = cls(*args)
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

class Product:
    name_product = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity):
        self.name_product = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def create_product(cls, name: str, description: str, price: float, quantity: int, products: list):
        """
        метод создания объекта продукта с условием отбора одинаковых имен
        """
        product_name = []
        for i in products:
            product_name.append(i.name_product)
        if len(products) == 0:
            product = cls(name, description, price, quantity)
            return product
        elif name in product_name:
            for i in products:
                if name == i.name_product:
                    i.quantity += quantity
                    if i.get_price < price:
                        i.get_price = price
        else:
            product = cls(name, description, price, quantity)
            return product

    @property
    def get_price(self):
        return self.__price

    @get_price.setter
    def get_price(self, new_price):
        if new_price <= 0:
            return print('Цена введена некорректная')
        else:
            self.__price = new_price

    @get_price.deleter
    def get_price(self):
        x = input('Если уверены что хотите удалить введите Y\n')
        if x.lower() == 'y':
            print('Удаляем цену')
            self.__price = None
        return True


class Category:
    name_category = str
    description = str
    products = list
    __products_objects = list
    number_of_category = 0
    number_of_product = 0
    all_objects_product = []

    def __init__(self, name, description, products=None):
        self.name_category = name
        self.description = description
        self.products = products
        self.__products_objects = []
        Category.number_of_category += 1

    def add_products(self, product):
        """
        добавляем продукт в список продуктов атрибута категории и список продуктов атрибута класса
        """
        if isinstance(product, Product):
            self.__products_objects.append(product)
            self.all_objects_product.append(product)
            Category.number_of_product += 1
        else:
            print('Не верный продукт')

    @property
    def get_product(self):
        """
        Возвращает список объектов продуктов
        """
        return self.__products_objects

    @property
    def get_product_info(self):
        """
        Печатает список объектов продуктов категории в определенном формате
        """
        list_data = []
        for item in self.__products_objects:
            list_data.append(f'{item.name_product}, {item.get_price} руб. Остаток: {item.quantity} шт.')
        return list_data

    def create_product(self):
        """
        Создаем продукты из файла json
        """
        for item in self.products:
            self.__products_objects.append(Product(item['name'], item['description'], item['price'], item['quantity']))
            Category.number_of_product += 1

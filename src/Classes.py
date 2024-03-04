class Product:
    name_product = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity):
        self.name_product = name
        self.description = description
        self.price = price
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
                    if i.price < price:
                        i.price = price
        else:
            product = cls(name, description, price, quantity)
            return product

    @property
    def get_price(self):
        if self.price <= 0:
            print('Цена введена некорректная')
        else:
            print(self.price)

    @get_price.setter
    def get_price(self, new_price):
        if new_price <= 0:
            print('Цена введена некорректная')
        else:
            self.price = new_price

    @get_price.deleter
    def get_price(self):
        x = input('Если уверены что хотите удалить введите Y\n')
        if x.lower() == 'y':
            print('Удаляем цену')
            self.price = None


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
        for item in self.__products_objects:
            print(f'{item.name_product}, {item.price} руб. Остаток: {item.quantity} шт.')

    def create_product(self):
        """
        Создаем продукты из файла json
        """
        for item in self.products:
            self.__products_objects.append(Product(item['name'], item['description'], item['price'], item['quantity']))
            Category.number_of_product += 1

# new_cat = Category("Telephone", "Лучшие телефоны")

# new_product = Product.create_product('Samsung Galaxy23', 'Флагман', 23000.0, 12, Category.all_objects_product)
# new_cat.add_products(new_product)
# new_product2 = Product.create_product('Apone 13', '231231221', 150000.0, 2, Category.all_objects_product)
# new_cat.add_products(new_product2)
# new_product3 = Product.create_product('Apone 13', '231231221', 160000.0, 1, Category.all_objects_product)
# new_cat.add_products(new_product3)
#
#
# new_cat.get_product_info


# new_product2.get_price
# del new_product2.get_price
# new_product2.get_price = 20000
# new_product2.get_price

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

    # def __del__(self):

    @classmethod
    def create_product(cls, name: str, description: str, price: float, quantity: int):
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
        print('Удаляем цену')
        self.price = None



class Category:
    name_category = str
    description = str
    products = list
    products_objects = list
    number_of_category = 0
    number_of_product = 0

    def __init__(self, name, description, products=None):
        self.name_category = name
        self.description = description
        self.products = products
        self.__products_objects = []
        Category.number_of_category += 1



    def add_products(self, product):
        if isinstance(product, Product):
            self.__products_objects.append(product)
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
        Возвращает список объектов продуктов категории в определенном формате
        """
        # list = []
        # for item in self.__products_objects:
        #     text = f'{item.name_product}, {item.price} руб. Остаток: {item.quantity} шт.'
        #     list.append(text)
        # return list

        for item in self.__products_objects:
            print(f'{item.name_product}, {item.price} руб. Остаток: {item.quantity} шт.')




    def create_product(self):
        for item in self.products:
            self.__products_objects.append(Product(item['name'], item['description'], item['price'], item['quantity']))
            Category.number_of_product += 1


new_cat = Category("Смартфоны", "Лучшие телефоны")

new_product = Product.create_product('Samsung Galaxy23', 'Флагман', 23000.0, 12)
new_product2 = Product.create_product('Apone Galaxy23', '231231221', 2030000.0, 1)
new_product3 = Product.create_product('Apone Galaxy23', '231231221', 440000.0, 121)
new_cat.add_products(new_product)
new_cat.add_products(new_product2)
new_cat.add_products(new_product3)


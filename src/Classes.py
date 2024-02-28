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


class Category:
    name_category = str
    description = str
    products = list
    products_objects = list
    number_of_category = 0
    number_of_product = 0

    def __init__(self, name, description, products):
        self.name_category = name
        self.description = description
        self.products = products
        self.products_objects = []
        Category.number_of_category += 1

    def create_product(self):
        for item in self.products:
            self.products_objects.append(Product(item['name'], item['description'], item['price'], item['quantity']))
            Category.number_of_product += 1

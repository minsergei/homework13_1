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
        self.__products_objects = []
        Category.number_of_category += 1

    def add_products(self, product):
        self.__products_objects.append(product)
        print(self.products_objectsproducts_objects)

    def create_product(self):
        for item in self.products:
            self.__products_objects.append(Product(item['name'], item['description'], item['price'], item['quantity']))
            Category.number_of_product += 1


x = Category("abs", "312312", "dsa")

x.add_products("gdfgdf")
print(x.name_category)
print(x.__products_objects)

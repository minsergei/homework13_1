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
    def create_product(cls, *args):
        """
        метод создания объекта продукта с условием отбора одинаковых имен
        """
        product_name = []
        for i in args[4]:
            product_name.append(i.name_product)
        if len(args[4]) == 0:
            product = cls(args[0], args[1], args[2], args[3])
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
            return print('Цена введена некорректная')
        else:
            self.__price = new_price

    @price.deleter
    def price(self):
        x = input('Если уверены что хотите удалить введите Y\n')
        if x.lower() == 'y':
            print('Удаляем цену')
            self.__price = None
        return True


class Category:
    name_category = str
    description = str
    __products = list
    number_of_category = 0
    number_of_product = 0
    all_objects_category = []
    all_objects_product = []

    def __init__(self, name, description):
        self.name_category = name
        self.description = description
        self.__products = []
        Category.number_of_category += 1

    @classmethod
    def create_category(cls, *args):
        """
        метод создания объекта категории с условием отбора одинаковых имен
        """
        category_name = []
        for i in args[2]:
            category_name.append(i.name_category)
        if len(args[2]) == 0:
            category = cls(args[0], args[1])
            Category.all_objects_category.append(category)
            return category
        elif args[0] in category_name:
            for i in args[2]:
                if args[0] == i.name_category:
                    break
        else:
            category = cls(args[0], args[1])
            Category.all_objects_category.append(category)
            return category
        print(category_name)

    def add_products(self, product):
        """
        добавляем продукт в список продуктов атрибута категории и список продуктов атрибута класса
        """
        if isinstance(product, Product):
            self.__products.append(product)
            self.all_objects_product.append(product)
            Category.number_of_product += 1
        else:
            print('Не верный продукт')

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

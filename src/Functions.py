import json
from src.Classes import Category, Product


def load_data(data):
    """
    загружаем данные из файла json
    """
    with open(data) as file:
        data_file = json.load(file)
    return data_file


def created_objects(data_file_load):
    """
    создаём объекты класса категории и объекты класса продукты в аргументах объекта класса категории по json файлу
    """

    for item in data_file_load:
        product_list = []
        for item2 in item['products']:
            new_product = Product.create_product(item2['name'], item2['description'], item2['price'],
                                                 item2['quantity'], Category.all_objects_product)
            if new_product:
                Category.all_objects_product.append(new_product)
                product_list.append(new_product)
        new_category = Category.create_category(item['name'], item['description'], product_list)
        for i in product_list:
            new_category.add_products_json(i)
    return None

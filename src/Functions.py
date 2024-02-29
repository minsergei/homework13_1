import json
from src.Classes import Category


def load_data(data):
    """
    загружаем данные из файла json
    """
    with open(data) as file:
        data_file = json.load(file)
    return data_file


def created_objects(data_file_load):
    """
    создаём объекты класса продукты в аргументах объекта класса категории
    """
    list_class_category = []
    for item in data_file_load:
        list_class_category.append(Category(item['name'], item['description'], item['products']))

    for item in list_class_category:
        item.create_product()

    return list_class_category

from pathlib import Path
from Classes import Category
from Functions import load_data, created_objects


def main():
    # Получаем путь файла json
    all_data = Path(__file__).parent.joinpath('products.json')
    # Загружаем данные из файла
    data_file_load = load_data(all_data)
    # Создаём объекты и получаем список объектов класса Категория
    list_class_category = created_objects(data_file_load)

    # Проверка заполнения классов объектами
    for item in list_class_category:
        if item.name_category == 'Смартфоны':
            print(f'{item.name_category}:\n')
            for item1 in item.products_objects:
                print(f'{item1.name_product} - {item1.description} - по цене {item1.price} руб - '
                      f'в количестве {item1.quantity} штук')

    print(f'\nКоличество объектов класса "Категория" - {Category.number_of_category}')
    print(f'Количество объектов класса "Продукты" - {Category.number_of_product}\n')

    for item in list_class_category:
        print(f'{item.name_category} - Объекты в категории {item.products_objects}')
    print(f'\nОбъекты категорий - {list_class_category}')


if __name__ == '__main__':
    main()

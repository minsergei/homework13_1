from pathlib import Path
from Classes import Category, Product
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
        print(item.description)
        products = item.get_product_info
        for i in range(len(products)):
            print(products[i])




    # print(f'\nКоличество объектов класса "Категория" - {Category.number_of_category}')
    # print(f'Количество объектов класса "Продукты" - {Category.number_of_product}\n')
    #
    # for item in list_class_category:
    #     print(f'{item.name_category} - Объекты в категории {item.get_product}')
    # print(f'\nОбъекты категорий - {list_class_category}')


if __name__ == '__main__':
    main()

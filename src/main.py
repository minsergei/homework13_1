from pathlib import Path
from src.Classes import Category, Product
from src.Functions import load_data, created_objects


def main():
    # Получаем путь файла json
    all_data = Path(__file__).parent.joinpath('products.json')
    # Загружаем данные из файла
    data_file_load = load_data(all_data)
    # Создаём объекты и получаем список объектов класса Категория
    list_class_category = created_objects(data_file_load)

    # Дальше код дополнительных проверок
    # Проверка заполнения классов объектами
    for item in list_class_category:
        print(item.name_category)
        print(*item.get_product_info)

    print(f'\nКоличество объектов класса "Категория" - {Category.number_of_category}')
    print(f'Количество объектов класса "Продукты" - {Category.number_of_product}\n')

    for item in list_class_category:
        print(f'{item.name_category} - Объекты в категории {item.get_product}')
    print(f'\nОбъекты категорий - {list_class_category}')
    # Создаём дополнительную категорию и продукты в ней
    new_cat = Category.create_category("Telephone", "Лучшие телефоны", Category.all_objects_category)
    new_cat2 = Category.create_category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни", Category.all_objects_category)
    new_product = Product.create_product('Samsung Galaxy23', 'Флагман', 23000.0, 12, Category.all_objects_product)
    new_cat.add_products(new_product)
    new_product2 = Product.create_product('Apone 13', 'The best', 150000.0, 1, Category.all_objects_product)
    new_cat.add_products(new_product2)
    new_product3 = Product.create_product('Apone 13', 'The best!!!', 160000.0, 2, Category.all_objects_product)
    new_cat.add_products(new_product3)
    # Считаем вместе количество категорий и продуктов, созданных из файла json и вручную
    print(f"{new_product2.name_product}: Цена {new_product2.price}, количество {new_product2.quantity}")
    print(Category.number_of_category)
    print(Category.number_of_product)


if __name__ == '__main__':
    main()

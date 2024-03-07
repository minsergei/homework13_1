from pathlib import Path
from src.Classes import Category, Product
from src.Functions import load_data, created_objects


def main():
    # Получаем путь файла json
    all_data = Path(__file__).parent.joinpath('products.json')
    # Загружаем данные из файла
    data_file_load = load_data(all_data)
    # Создаём объекты и получаем список объектов класса Категория
    created_objects(data_file_load)

    # Дальше код дополнительных проверок
    # Подгрузим еще один файла json с другими категориями и продуктами, в том числе повторяющиеся
    all_data = Path(__file__).parent.joinpath('products2.json')
    data_file_load = load_data(all_data)
    created_objects(data_file_load)

    # Создаём дополнительную категорию и продукты в ней
    new_cat = Category.create_category("Telephone", "Лучшие телефоны", Category.all_objects_category)
    # Создаём дополнительную категорию с названием которое уже есть. Она не добавится
    new_cat2 = Category.create_category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и "
                                                     "получение дополнительных функций для удобства жизни",
                                        Category.all_objects_category)

    new_product = Product.create_product('Samsung Galaxy23', 'Флагман', 23000.0, 12, Category.all_objects_product)
    new_cat2.add_products(new_product)
    new_product2 = Product.create_product('Apone 13', 'The best', 150000.0, 1, Category.all_objects_product)
    new_cat.add_products(new_product2)
    # Создаём доп. продукт с названием которое уже есть. Он не добавится. Но цена и количество будут обрабатываться
    new_product3 = Product.create_product('Apone 13', 'The best!!!', 160000.0, 2, Category.all_objects_product)
    new_cat.add_products(new_product3)

    # Считаем вместе количество категорий и продуктов, созданных из файла json и вручную
    print(f'Количество категорий - {Category.number_of_category}')
    print(f'Количество продуктов - {Category.number_of_product}')
    # Проверка __str__ и __len__
    for item in Category.all_objects_category:
        print(f'_________________________________\n{item}\n---------------------------------')
        for item2 in item.get_product:
            print(f'    {item2}')


if __name__ == '__main__':
    main()

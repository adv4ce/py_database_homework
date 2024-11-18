from psycopg2 import *
from client import *
from create_database import *
from params import params
from find_and_delete import *


def delete_test_table():
    with connect(**params) as conn:
        with conn.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS client;")


def create_command(command):
    try:
        with connect(**params) as conn:
            with conn.cursor() as cursor:
                cursor.execute(command)
                return cursor.fetchall()
    except Error as error:
        print(f"При запросе произошла ошибка: {error}")


def main():
    # Создание таблицы
    create_database()

    client = Client()
    # Добавление нового клиента
    client.add_new_client(
        "Виктория", "Румянцева", "rumviktoria@gmail.com", "89775134762"
    )
    client.add_new_client("Ярослав", "Васильев", "vasyaroslav@mail.ru", "89030187944")
    client.add_new_client("Александра", "Коровина", "koraleks@yandex.ru", "")
    client.add_new_client("Марк", "Леонов", "leonmark@yandex.ru", "89265406986")

    cursor = create_command("SELECT * FROM client;")
    print("Добавление нового клиента:\n", f"{cursor}\n")

    # Добавление телефона существующему клиенту
    client.add_phone_number_to_existing_client("Александра", "Коровина")

    cursor = create_command("SELECT * FROM client;")
    print("Добавление телефона существующему клиенту:\n", f"{cursor}\n")

    # Изменение данных клиента
    menu = change_client_menu()
    data = input_data(menu)
    client.change_client_data(data, menu)

    cursor = create_command("SELECT * FROM client;")
    print("Изменение данных клиента:\n", f"{cursor}\n")

    # Удаление телефона клиента
    client.delete_phone("Александра", "Коровина")

    cursor = create_command("SELECT * FROM client;")
    print("Удаление телефона клиента:\n", f"{cursor}\n")

    # Удаление клиента
    menu = select_points()
    data = input_data(menu)
    client.delete_client(data, menu)

    cursor = create_command("SELECT * FROM client;")
    print("Удаление клиента:\n", f"{cursor}\n")

    # Поиск клиента
    menu = select_points()
    data = input_data(menu)
    client.find_client(data, menu)


if __name__ == "__main__":
    delete_test_table()
    main()

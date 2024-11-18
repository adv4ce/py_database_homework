from psycopg2 import *
from params import params
from find_and_delete import *


class Client:
    def add_new_client(self, name, surname, email, phone):
        try:
            with connect(**params) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO client(name, surname, email, phone) VALUES(%s, %s, %s, %s);",
                        (name, surname, email, phone),
                    )
                    print(
                        f"Клиент: {name} {surname}, {email}, {phone} успешно добавлен"
                    )

        except Error as error:
            print(f"При выполнении запроса произошла ошибка: {error}")

    def add_phone_number_to_existing_client(self, name, surname):
        try:
            with connect(**params) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM client WHERE name = %s AND surname = %s;",
                        (name, surname),
                    )
                    result = cursor.fetchone()
                    if result:
                        new_phone = input("Введите новый номер телефона: ")
                        cursor.execute(
                            "UPDATE client SET phone = %s WHERE name = %s AND surname = %s;",
                            (new_phone, name, surname),
                        )
                        print("Номер телефона успешно изменен")

                    else:
                        print(f"Клиента с инициалами: {name} {surname} не существует")

        except Error as error:
            print(f"При выполнении запроса произошла ошибка: {error}")

    def change_client_data(self, data, menu):
        try:
            with connect(**params) as conn:
                with conn.cursor() as cursor:
                    values = {"1": "name", "2": "surname", "3": "email", "4": "phone"}
                    find_client = select_points()
                    req_txt = " AND ".join(
                        [values[i] + "=%s" for i in find_client]
                    )
                    req_val = [i for i in input_data(find_client)]
                    req_val = tuple(req_val)
                    change = ", ".join([values[i] + "=%s" for i in menu])
                    client_new_info = tuple([i for i in data])

                    with connect(**params) as conn:
                        with conn.cursor() as cursor:
                            cursor.execute(
                                f"UPDATE client SET {change} WHERE {req_txt}",
                                client_new_info + req_val,
                            )

        except Error as error:
            print(f"При выполнении запроса произошла ошибка: {error}")

    def delete_phone(self, name, surname):
        try:
            with connect(**params) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM client WHERE name = %s AND surname = %s;",
                        (name, surname),
                    )
                    result = cursor.fetchone()
                    if result:
                        cursor.execute(
                            "UPDATE client SET phone = NULL WHERE name = %s AND surname = %s;",
                            (name, surname),
                        )
                        print(f"Телефон клиента {name} {surname} успешно удален")

                    else:
                        print(f"Клиента с инициалами: {name} {surname} не существует")

        except Error as error:
            print(f"При выполнении запроса произошла ошибка: {error}")

    def delete_client(self, data, menu):
        try:
            values = {"1": "name", "2": "surname", "3": "email", "4": "phone"}
            req_txt = " AND ".join([values[i] + "=%s" for i in menu])
            req_val = [i for i in data]
            req_val = tuple(req_val)
            with connect(**params) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(f"SELECT * FROM client WHERE {req_txt}", req_val)
                    find_clients = cursor.fetchall()
                    if len(find_clients) != 0:
                        cliend_delete_menu = delete_client_menu(find_clients)
                        for i in cliend_delete_menu:
                            cursor.execute("DELETE FROM client WHERE id=%s", (i))
                        return "Выбраные клиенты удалены"
                    else:
                        return "Клиентов с такими данными не найдено"

        except Error as error:
            print(f"При выполнении запроса произошла ошибка: {error}")

    def find_client(self, data, menu):
        try:
            with connect(**params) as conn:
                with conn.cursor() as cursor:
                    values = {"1": "name", "2": "surname", "3": "email", "4": "phone"}
                    req_txt = " AND ".join([values[i] + "=%s" for i in menu])
                    req_val = [i for i in data]
                    req_val = tuple(req_val)
                    with connect(**params) as conn:
                        with conn.cursor() as cursor:
                            cursor.execute(
                                f"SELECT * FROM client WHERE {req_txt}",
                                req_val,
                            )
                            return print_clients(cursor.fetchall())

        except Error as error:
            print(f"При выполнении запроса произошла ошибка: {error}")

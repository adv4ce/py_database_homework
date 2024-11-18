from prompt_toolkit.shortcuts import checkboxlist_dialog
from params import params
from psycopg2 import *
from tabulate import *


def select_points(text="Выберите пункты, по которым хотите найти клиента: "):
    points = [("1", "name"), ("2", "surname"), ("3", "email"), ("4", "phone")]
    menu = checkboxlist_dialog(
        title="Menu",
        text=text,
        values=points,
    ).run()

    if len(menu) == 0:
        menu = select_points("Выберите хотя бы один пункт!")

    return menu


def input_data(data):
    name = ""
    surname = ""
    email = ""
    phone = ""

    for i in data:
        if i == "1":
            name = input("Введите имя: ")

        elif i == "2":
            surname = input("Введите фамилию: ")

        elif i == "3":
            email = input("Введите email: ")

        elif i == "4":
            phone = input("Введите номер телефона: ")

    return [i for i in [name, surname, email, phone] if len(i) > 0]


def print_clients(client_list):
    header = ["ID", "Name", "Surname", "Email", "Phone"]
    data = [list(i) for i in client_list]
    print(tabulate(data, headers=header, tablefmt="grid"))


def delete_client_menu(data, text="Выберите клиента(-ов) для удаления"):
    client_info = [
        (t[0], f"Имя: {t[1]}, Фамилия: {t[2]}, Почта: {t[3]}, Телефон: {t[4]}")
        for t in data
    ]
    menu = checkboxlist_dialog(
        title="Menu",
        text=text,
        values=[tuple(str(j) for j in i) for i in client_info],
    ).run()

    if len(menu) == 0:
        menu = delete_client_menu(data, text="Выберите хотя бы один пункт!")

    return menu


def change_client_menu(text="Выберите поле(-я) для изменения"):
    points = [("1", "name"), ("2", "surname"), ("3", "email"), ("4", "phone")]
    menu = checkboxlist_dialog(
        title="Menu",
        text=text,
        values=points,
    ).run()

    if len(menu) == 0:
        menu = change_client_menu("Выберите хотя бы один пункт!")

    return menu

def input_change_data(data):
    name = ""
    surname = ""
    email = ""
    phone = ""

    for i in data:
        if i == "1":
            name = input("Введите новое имя: ")

        elif i == "2":
            surname = input("Введите новую фамилию: ")

        elif i == "3":
            email = input("Введите новый email: ")

        elif i == "4":
            phone = input("Введите новый номер телефона: ")

    return [i for i in [name, surname, email, phone] if len(i) > 0]

from psycopg2 import *
from params import params


def create_database():
    try:
        with connect(**params) as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS client(
                            id SERIAL PRIMARY KEY,
                            name VARCHAR(100) NOT NULL,
                            surname VARCHAR(100) NOT NULL,
                            email VARCHAR(100) NOT NULL,
                            phone VARCHAR(50))"""
                )
                conn.commit()
                return "Таблица успешно создана"

    except Error as error:
        return f"При выполнении запроса произошла ошибка: {error}"

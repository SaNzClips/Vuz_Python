# Лаба 6 №5
# Написать функцию, которая принимает словарь, в которой ключами являются наименования таблиц, а значениями 
# список списков, содержащих данные для таблицы, и выполняет 
# вставку полученных данных в указанные таблицы.

import sqlite3

def insert_data_into_tables(data_dict, database_path): #Функция принимает словарь с данными и путь к базе данных. Выполняет вставку данных в соответствующие таблицы.
    
    global connection
    try:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        for table_name, data_rows in data_dict.items():
            # Создаем таблицу, если её нет
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, name TEXT, value INTEGER);")

            # Вставляем данные в таблицу
            cursor.executemany(f"INSERT INTO {table_name} (name, value) VALUES (?, ?);", data_rows)

        connection.commit()
        print("Данные вставлены в таблицы.")
    except sqlite3.Error as e:
        print(f"Ошибка при работе с базой данных: {e}")
    finally:
        if connection:
            connection.close()

# Пример использования функции:
data_to_insert = {
    'table1': [('John', 25), ('Alice', 30), ('Bob', 22)],
    'table2': [('Anna', 100), ('Tom', 150), ('Eva', 120)]
}

database_path = 'example.db'
insert_data_into_tables(data_to_insert, database_path)

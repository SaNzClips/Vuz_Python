# Лаба 4 Задание №15
# Написать функцию относительно задания 8, которая
# принимает созданные 20 объектов datetime и создает для значе-
# ний года, месяца и дня вложенные директории. Например, зна-
# чение 2019-09-02 создаст три директории. Корневой будет
# 2019, внутри неё 09 и т.д. Стоит отметить, что значение другого
# объекта 2019-07-02 создаст в ранее созданной директории 2019
# директорию с наименованием 07.

from datetime import datetime, timedelta
import os

def generate_date_list(x):

    current_date = datetime.now()  # Текущая дата и время
    date_list = []

    for _ in range(20):
        date_list.append(current_date)
        current_date += timedelta(days=x)

    return date_list

def create_nested_directories(date_list):

    for date_obj in date_list:
        year = str(date_obj.year)
        month = str(date_obj.month).zfill(2)  # Заполняем нулями слева, если месяц < 10
        day = str(date_obj.day).zfill(2)  # Заполняем нулями слева, если день < 10

        directory_path = os.path.join(year, month, day)

        # Проверяем, существует ли уже такая директория
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

interval_days = 2
date_list_result = generate_date_list(interval_days)

# Создаем вложенные директории
create_nested_directories(date_list_result)
# Лаба 2 Задание №5
# Написать функцию, которая принимает список, состо-
# ящий из строк, которые являются целочисленными значениями
# или значениями с плавающей точкой, и возвращает их сумму.

# -*- coding: utf-8 -*-

def sum_values(input_list):
    print("Функция принимает список строк с числами и возвращает их сумму.")
    total_sum = 0

    for value in input_list:
        try:
            total_sum += float(value)
        except ValueError:
            pass

    return total_sum

my_list = ["2", "1.2", "1", "4.6", "7"]
result = sum_values(my_list)
print(result)

# Лаба 1 Задание №15
# Написать функцию, которая принимает на вход список,
# состоящий из n различных элементов. Вернуть словарь, в кото-
# ром ключами являются элементы входящего списка, а их зна-
# чениями – число повторений этих элементов во входящем списке.

# -*- coding: utf-8 -*-

def count_elements(lst):
    element_count = {}
    for element in lst:
        element_count[element] = element_count.get(element, 0) + 1
    return element_count

my_list = [1, 2, 3, 2, 1, 3, 4, 5]
result = count_elements(my_list)
print(result)

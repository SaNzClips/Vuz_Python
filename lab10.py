def no_zeros(lst):
    return all(x != 0 for x in lst)

# Пример использования
my_list = [1, 2, 3, 9, 4, 5]
result = no_zeros(my_list)
print(result)

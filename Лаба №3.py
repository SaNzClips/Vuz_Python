# Лаба 3 Задание №15
# Написать функцию, которая принимает строку и с по-
# мощью генераторного выражения создает список, в котором
# все символы входящей строки смещены на один символ вправо
# по алфавиту, кроме символов от «ы» до «я». Требуется вернуть
# строку из созданного списка.

def shift_characters(input_str):
    result_str = ""

    for char in input_str:
        if 'а' <= char <= 'ы':
            shifted_char = chr((ord(char) - ord('а') + 1) % 32 + ord('а'))
            result_str += shifted_char
        else:
            result_str += char

    return result_str

original_str = "корень имбиря"
result_str = shift_characters(original_str)
print(result_str)

# Лаба 5 №2
# Написать функцию, которая принимает путь к файлу и 
# количество строк, которые требуется прочитать и возвращает 
# считанные строки в файле.

def read_file_lines(file_path, num_lines):
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [next(file).strip() for _ in range(num_lines)]
        return lines
    except FileNotFoundError:
        return f"Файл {file_path} не найден."
    except Exception as e:
        return f"Произошла ошибка при чтении файла: {str(e)}"

file_path = r'C:\Users\Kolya\OneDrive\Рабочий стол\Vuz\python\labs pypkasnd\Тест текст.txt'
num_lines_to_read =8
result_lines = read_file_lines(file_path, num_lines_to_read)

for line in result_lines:
    print(line)

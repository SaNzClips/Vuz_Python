# Лаба 8 №1
# Написать функцию, которая принимает путь к директории и создает новую директорию по тому же пути с именем 
# thumbnail, в которую записывает иконки изображений, находящихся в принятой функцией директории

import os
from PIL import Image

def create_thumbnail_directory(directory_path):
    thumbnail_dir = os.path.join(directory_path, 'thumbnail')

    # Проверяем, существует ли уже директория thumbnail
    if not os.path.exists(thumbnail_dir):
        os.makedirs(thumbnail_dir)

    # Получаем список файлов в директории
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    # Обрабатываем изображения и создаем миниатюры
    for file_name in files:
        file_path = os.path.join(directory_path, file_name)

        # Проверяем, что файл - изображение
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            try:
                image = Image.open(file_path)
                thumbnail = image.thumbnail((100, 100))  # Указываем размер миниатюры (ширина, высота)
                thumbnail_path = os.path.join(thumbnail_dir, f"thumbnail_{file_name}")
                image.save(thumbnail_path)
                print(f"Создана миниатюра для файла: {file_name}")
            except Exception as e:
                print(f"Ошибка при создании миниатюры для файла {file_name}: {str(e)}")

# Пример использования функции:
directory_path = r'C:\Users\Kolya\OneDrive\Рабочий стол\Vuz\python\labs pypkasnd\IMGshka'
create_thumbnail_directory(directory_path)

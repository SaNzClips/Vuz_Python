# Лаба 7 №5
# Написать класс UserLanguagePreference, который в конструкторе принимает список языков в виде строки,
# которые используют пользователи и содержит метод add_lang(lang_str),
# который добавляет язык в список, если его там не существует.
# Данный класс использует инкапсуляцию, для получения используемого списка


class UserLanguagePreference:
    def __init__(self, languages_str):
        self._languages = languages_str.split(',')

    def get_languages(self):
        """Возвращает список языков."""
        return self._languages

    def add_lang(self, lang_str):
        lang = lang_str.strip()
        """Добавляет язык в список, если его там нет."""
        if lang not in self._languages:
            self._languages.append(lang)
            print(f"Язык {lang} добавлен.")
        else:
            print(f"Язык {lang} уже существует в списке.")

# Пример использования класса:
user_pref = UserLanguagePreference("English,French,Spanish")

# Получаем и выводим список языков
print("Исходный список языков:", user_pref.get_languages())

# Добавляем новый язык
user_pref.add_lang("German")

# Добавляем существующий язык
user_pref.add_lang("French")

# Получаем и выводим обновленный список языков
print("Обновленный список языков:", user_pref.get_languages())

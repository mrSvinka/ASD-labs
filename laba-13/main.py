"""
Дан текстовый файл с некоторым текстом на русском или английском языках произвольной длины (организовать чтение).
Выбрав некоторую хеш-функцию, создать хеш-таблицу с:

Лаба №13 “с наложением”
"""

class HashTable:
    def __init__(self, size=73):  ## Конструктор класса, инициализирует хеш-таблицу
        self.size = size  ## Размер таблицы
        self.table = [None] * size  ## Создание массива
        self.count = 0  ## Счетчик количества элементов

    def hash_function(self, key): ##Хеш-функция для строк: сумма кодов символов по модулю размера таблицы
        return sum(ord(char) for char in
                   key) % self.size  ## Суммируем коды, остаток от деления

    def linear_probing(self, key, i): ##Линейное пробирование для разрешения коллизий
        return (self.hash_function(key) + i) % self.size  ## Hовый индекс

    def insert(self, key): ##Линейное пробирование (добав. элемента)
        if self.count >= self.size:  ## Проверка на переполнение таблицы
            raise Exception("Хеш-таблица переполнена")

        i = 0
        while i < self.size:
            index = self.linear_probing(key, i)  ## индекс с учетом пробирования

            if self.table[index] is None:  ## Если ячейка пустая
                self.table[index] = (key, 1)  ## ключ, количество
                self.count += 1
                return
            elif self.table[index][0] == key:  ## Если ключ существует в таблице
                key, count = self.table[index]  ## Извлекаем запись
                self.table[index] = (key, count + 1)
                return
            else:  ## Если произошла коллизия с другим ключом
                i += 1

        raise Exception("Не удалось найти свободную ячейку")  ## Если не нашли место

    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:

            ## Заголовок таблицы
            file.write("Индекс | Слово (количество)\n")

            ## Статистические переменные
            total_words = 0  ## Общее количество слов
            collisions = 0  ## Количество коллизий
            occupied_cells = 0  ## Количество занятых ячеек

            ## Проходим по всем ячейкам таблицы
            for i, item in enumerate(self.table):
                if item is not None:  ## Если ячейка не пустая
                    occupied_cells += 1  ## Увеличиваем счетчик занятых ячеек
                    word, count = item  ## Распаковка
                    file.write(f"{i:6} | '{word}' ({count})\n")  ## Записываем данные
                    total_words += count

                    ## является ли позиция коллизией
                    original_index = self.hash_function(word)  ## Вычисляем исходный хеш-индекс
                    if original_index != i:
                        collisions += 1
                        file.write(f"       | [Коллизия. Оригинальный индекс: {original_index}]\n")
                else:  ## Если ячейка пустая
                    file.write(f"{i:6} | - пусто -\n")

def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        ## Разделяем на слова и очищаем от знаков препинания
        words = []  
        for word in text.split():  ## Разбиваем текст на слова
            clean_word = word.strip('.,!?;:()"').lower()  ## Удаляем знаки препинания и приводим к нижнему регистру
            if clean_word:  ## Если слово не пустое после очистки
                words.append(clean_word)  ## Добавляем слово в список
        return words
    except FileNotFoundError:  ## Обработка исключения, если файл не найден
        print(f"Файл {filename} не найден")
        return []


def main():
    input_filename = "russian_text.txt"
    output_filename = "hash_table_result.txt"

    words = read_file(input_filename)

    if not words:
        return

    # Создание хеш-таблицы
    hash_table = HashTable(size=73)

    # Добавление слов в хеш-таблицу
    for word in words:
        hash_table.insert(word)

    # Сохранение
    hash_table.save_to_file(output_filename)

if __name__ == "__main__":
    main()
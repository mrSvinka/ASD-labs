"""
Дан текстовый файл с некоторым текстом на русском или английском языках произвольной длины (организовать чтение).
Выбрав некоторую хеш-функцию, создать хеш-таблицу с:

Лаба №13 “с наложением”
"""

class HashTableChaining:
    def __init__(self, size=10): ##Инициализация хеш-таблицы со списками
        self.size = size  # Размер таблицы
        self.table = [[] for _ in range(size)]  # Создаем список
        self.total_words = 0  # количество слов
        self.unique_words = 0  # Количество уникальных слов

    def hash_function(self, key): ##Хеш-функция для строк: сумма кодов символов по модулю размера таблицы
        return sum(ord(char) for char in key) % self.size  # Сумма кодов символов по модулю размера таблицы

    def insert(self, key):##Добавление элемента в хеш-таблицу методом цепочек
        index = self.hash_function(key)  ##индекс с помощью хеш-функции
        bucket = self.table[index]  # Получаем список по вычисленному индексу

        # Проверяем, есть ли уже такой ключ
        for i, (k, count) in enumerate(bucket):
            if k == key:  # Если ключ уже существует
                bucket[i] = (k, count + 1)  # Увеличиваем счетчик
                self.total_words += 1  # Увеличиваем общий счетчик слов
                return

        # Если ключа нет в бакете, добавляем новый элемент
        bucket.append((key, 1))  # Добавляем ключ, количество
        self.total_words += 1
        self.unique_words += 1

    def search(self, key): ##Поиск элемента в хеш-таблице
        index = self.hash_function(key)  # индекс с помощью хеш-функции
        bucket = self.table[index]  # Получаем

        # Ищем ключ
        for k, count in bucket:
            if k == key:  # Если нашли ключ
                return count

        return None  # Если ключ не найден

    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:  # Открываем файл для записи

            # Заголовок таблицы
            file.write("Индекс | Длина цепочки | Элементы цепочки\n")


            # Статистические переменные
            max_chain_length = 0  # Максимальная длина цепочки
            empty_buckets = 0  # Количество пустых бакетов
            total_chains_length = 0  # Общая длина всех цепочек
            non_empty_buckets = 0  # Количество непустых бакетов

            # Проходим по всей таблицы
            for i, bucket in enumerate(self.table):
                chain_length = len(bucket)  # Длина текущей цепочки
                total_chains_length += chain_length  # Увеличиваем общую длину цепочек

                if chain_length > max_chain_length:  # Обновляем максимальную длину цепочки
                    max_chain_length = chain_length

                if chain_length == 0:  # Если пустой
                    empty_buckets += 1
                    file.write(f"{i:6} | {chain_length:13} | - пусто -\n")
                else:  # Если бакет не
                    non_empty_buckets += 1
                    # Формируем строку
                    chain_elements = " → ".join([f"'{word}'({count})" for word, count in bucket])
                    file.write(f"{i:6} | {chain_length:13} | {chain_elements}\n")

def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        # Разделяем на слова и очищаем от знаков препинания
        words = []
        for word in text.split():  # Разбиваем текст на слова
            clean_word = word.strip('.,!?;:()"').lower()  # Удаляем знаки препинания и приводим к нижнему регистру
            if clean_word:  # Если слово не пустое после очистки
                words.append(clean_word)  # Добавляем слово в список
        return words
    except FileNotFoundError:  # Обработка исключения, если файл не найден
        print(f"Файл {filename} не найден")
        return []


def main():
    input_filename = "russian_text.txt"
    output_filename = "hash_table_chaining_result.txt"

    words = read_file(input_filename)  # Чтение слов из файла

    if not words:
        return

    # Создание хеш-таблицы
    hash_table = HashTableChaining(size=15)

    # Добавление слов в хеш-таблицу
    for word in words:
        hash_table.insert(word)

    # Сохранение
    hash_table.save_to_file(output_filename)

if __name__ == "__main__":
    main()
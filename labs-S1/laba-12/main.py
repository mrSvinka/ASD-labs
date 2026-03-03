#Дана последовательность чисел. Отсортировать и вывести последовательность чисел. Сортировка  Внешняя многофазная.

def external_multiway_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Создаём временные файлы
    temp_files = []
    num_files = 3  # Используем 3 файла

    for _ in range(num_files):
        temp_files.append([])

    # распределяем данные во временные файлы
    i = 0
    for num in arr:
        temp_files[i % num_files].append(num)
        i += 1

    # Сортируем каждый временный файл
    for i in range(num_files):
        temp_files[i] = sorted(temp_files[i])

    # Фаза слияния: объединяем файлы попарно
    while len(temp_files) > 1:
        new_temp_files = []
        for i in range(0, len(temp_files), 2):
            if i + 1 < len(temp_files):
                merged = merge(temp_files[i], temp_files[i + 1])
                new_temp_files.append(merged)
            else:
                new_temp_files.append(temp_files[i])
        temp_files = new_temp_files

    return temp_files[0]

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


arr = [8, 4, 1, 3, 2, 7, 6, 5, 9, 10]
sorted_arr = external_multiway_merge_sort(arr)
print("Отсортированная последовательность:", sorted_arr)
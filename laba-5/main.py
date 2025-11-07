##Дана последовательность чисел.Отсортировать и вывести последовательность чисел. Сортировка методом Вставками


def insertion_sort_detailed(arr):
    for i in range(1, len(arr)):
        key = arr[i] # Текущий элемент для вставки
        j = i - 1

        # Сдвигаем элементы больше key вправо
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [8, 4, 1, 3, 2, 7, 6, 5, 9, 10]
sorted_arr = insertion_sort_detailed(arr)
print(f"Финальный отсортированный массив: {sorted_arr}")

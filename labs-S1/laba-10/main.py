##Дана последовательность чисел. Отсортировать и вывести последовательность чисел. Сортировка  Слиянием.

def sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Находим середину массива
        left = arr[:mid]     # Делим массив на две части
        right = arr[mid:]

        sort(left)     # Рекурсивно сортируем левую часть
        sort(right)    # Рекурсивно сортируем правую часть

        # Слияние отсортированных частей
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Добавляем элементы из left или right
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


arr = [8, 4, 1, 3, 2, 7, 6, 5, 9, 10]
sort(arr)
print("Отсортированный массив:", arr)
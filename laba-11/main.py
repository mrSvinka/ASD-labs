#Дана последовательность чисел. Отсортировать и вывести последовательность чисел. Сортировка  Быстрая.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Выбор опорного элемента (середина массива)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr = [8, 4, 1, 3, 2, 7, 6, 5, 9, 10]
sorted_arr = quick_sort(arr)
print("Отсортированная последовательность:", sorted_arr)
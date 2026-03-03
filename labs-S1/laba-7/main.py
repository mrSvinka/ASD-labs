##Дана последовательность чисел. Отсортировать и вывести последовательность чисел. Сортировка методом Посредством выбора

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


arr = [8, 4, 1, 3, 2, 7, 6, 5, 9, 10]
selection_sort(arr)
print("Отсортированный массив:", arr)
##Дана последовательность чисел. Отсортировать и вывести последовательность чисел. Сортировка  Пирамидальная (heap sort).

def heapify(arr, n, i):
    largest = i  # Корень поддерева
    left = 2 * i + 1  # Левый потомок
    right = 2 * i + 2  # Правый потомок

    # Если левый потомок существует и больше корня
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Если правый потомок существует и больше текущего наибольшего
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Если наибольший элемент не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Построение max-кучи
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Последовательное извлечение элементов из кучи
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


arr = [8, 4, 1, 3, 2, 7, 6, 5, 9, 10]
heap_sort(arr)
print("Отсортированный массив:", arr)
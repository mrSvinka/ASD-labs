## Дана последовательность чисел. Отсортировать и вывести последовательность чисел. Сортировка методом прочесывания

def sort(arr):
    n = len(arr) ##длина
    step = n ##первый шаг
    swapped = True

    while step > 1 or swapped:
        step = max(1, int(step / 1.247))
        swapped = False
        for i in range(n - step):
            if arr[i] > arr[i + step]:
                arr[i], arr[i + step] = arr[i + step], arr[i]
                swapped = True



arr = [8, 4, 1, 3, 2, 7, 6, 5, 9, 10]
sort(arr)
print("Отсортированный массив:", arr)

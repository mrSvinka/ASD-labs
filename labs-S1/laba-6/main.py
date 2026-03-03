##Дана последовательность чисел. Отсортировать и вывести последовательность чисел. Сортировка методом Шелла

def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2


arr = [8, 4, 1, 3, 2, 7, 6, 5, 9, 10]
shell_sort(arr)
print("Отсортированный массив:", arr)
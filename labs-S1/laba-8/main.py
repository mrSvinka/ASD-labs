##Дана последовательность чисел. Отсортировать и вывести последовательность чисел. Сортировка  Поразрядная



def radix_sort(arr):
    if not arr:
        return arr

    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        # Создаем корзины
        buckets = [[] for _ in range(10)]

        # Распределяем, в зависимости от текущего разряда
        for num in arr:
            digit = (num // exp) % 10
            buckets[digit].append(num)

        # Собираем числа в массив
        arr = []
        for bucket in buckets:
            arr.extend(bucket)

        #К следующему разряду
        exp *= 10

    return arr



arr = [8, 4, 1, 3, 2, 7, 6, 5, 9, 10]
sorted_arr = radix_sort(arr)
print("Отсортированный массив:", sorted_arr)
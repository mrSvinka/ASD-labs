import bisect


def lis_length(arr):
    if not arr:
        return 0
    tails = []    #минимальные последние элементы для каждой длины
    for x in arr:
        idx = bisect.bisect_left(tails, x)
        if idx == len(tails):
            tails.append(x)
        else:
            tails[idx] = x
    return len(tails)


def lis_sequence(arr):
    if not arr:
        return []

    n = len(arr)
    tails = []          # значения
    tail_indices = []   # индексы в arr
    prev = [-1] * n     # prev[i] — индекс предыдущего элемента

    for i, x in enumerate(arr):
        idx = bisect.bisect_left(tails, x)   # O(log n)

        if idx == len(tails): # Обновляем длины idx+1
            tails.append(x)
            tail_indices.append(i)
        else:
            tails[idx] = x
            tail_indices[idx] = i

        if idx > 0: # Запоминаем предшественника (если длина > 1)
            prev[i] = tail_indices[idx - 1]

    # Восстановление последовательности с конца
    lis_len = len(tail_indices)
    seq_indices = []
    k = tail_indices[-1]
    for _ in range(lis_len):
        seq_indices.append(k)
        k = prev[k]
    seq_indices.reverse()
    return [arr[i] for i in seq_indices]


def main():
    tests = [
        [10, 22, 9, 33, 21, 50, 41, 60, 80],
        [-5, -2, -1, -4],
        [5, 4, -1, 7, 8],
        [],
        [3, 3, 3, 3],
        [1, 3, 6, 7, 9, 4, 10, 5, 6, 11]
    ]
    for arr in tests:
        length = lis_length(arr)
        seq = lis_sequence(arr)
        print(f"Массив: {arr}")
        print(f"Длина LIS: {length}")
        print(f"LIS: {seq}\n")


if __name__ == "__main__":
    main()
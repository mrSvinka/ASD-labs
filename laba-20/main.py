'''
Вам дан массив из n натуральных чисел и число k. Посчитайте количество пар индексов i j,
 таких что 1 i<j n, и ai+aj делится на k.
 Формат входных данных
 В первой строке вам дано число 1
n
2 105– количество элементов массива и число
 1 k 105.Вследующей строке вам даны элементы массива 1 ai 105.
 Формат выходных данных
 Выведите количество пар чисел, сумма которых делится на k.
'''


def count():
    import sys

    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    k = int(data[1])
    arr = list(map(int, data[2:2 + n]))

    # Массив для подсчета остатко
    remainder_count = [0] * k

    # Количество чисел для каждого остатка
    for num in arr:
        remainder_count[num % k] += 1

    # Счетчик пар
    pairs_count = 0

    # Обрабатываем остаток 0
    count0 = remainder_count[0]
    pairs_count += count0 * (count0 - 1) // 2

    # Если k четное
    if k % 2 == 0:
        count_mid = remainder_count[k // 2]
        pairs_count += count_mid * (count_mid - 1) // 2

    # Обрабатываем остальные остатки
    for r in range(1, (k + 1) // 2):
        if r != k - r:
            pairs_count += remainder_count[r] * remainder_count[k - r]

    print(pairs_count)


if __name__ == "__main__":
    count()




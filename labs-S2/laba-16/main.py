def exact_bin_packing(items, bin_capacity):
    n = len(items)
    if n == 0:
        return 0, []
    total = 1 << n
    INF = float('inf')

    dp = [(INF, INF)] * total     #количество ящиков, занятое место
    prev = [(-1, -1)] * total

    dp[0] = (1, 0) #1 ящик открыт, в нем 0 занято

    for mask in range(total):
        bins_used, used_space = dp[mask]

        if bins_used == INF:
            continue

        for i in range(n):  # Если i-й предмет еще не взят
            if not (mask & (1 << i)):
                new_mask = mask | (1 << i)
                sz = items[i]

                if used_space + sz <= bin_capacity: # Пытаемся положить в текущий ящик
                    new_bins = bins_used
                    new_used = used_space + sz
                # Если не влезает, новый ящик
                else:
                    new_bins = bins_used + 1
                    new_used = sz

                if (new_bins, new_used) < dp[new_mask]:
                    dp[new_mask] = (new_bins, new_used)
                    prev[new_mask] = (mask, i)

    if dp[total - 1][0] == INF:
        return None, None

    # Восстановление раскладки
    mask = total - 1
    bins = []
    cur_bin = []

    while mask > 0:
        prev_mask, i = prev[mask]

        cur_bin.append(items[i]) # Добавляем предмет в текущий ящик

        # Если шаг назад уменьшает количество ящиков, значит этот предмет был первым в этом ящике.
        if dp[mask][0] > dp[prev_mask][0]:
            bins.append(cur_bin[::-1])  # разворачиваем для хронологического порядка
            cur_bin = []

        mask = prev_mask


    if cur_bin: # Добавляем последний оставшийся ящик
        bins.append(cur_bin[::-1])

    bins.reverse()  # Разворачиваем список ящиков

    return dp[total - 1][0], bins


def main():
    try:
        n = int(input("Количество предметов: "))
        items = list(map(int, input("Размеры предметов: ").split()))
        if len(items) != n:
            items = items[:n]
        bin_capacity = int(input("Вместимость ящика: "))
    except ValueError:
        print("Ошибка!")
        return

    if any(s > bin_capacity for s in items):
        print("Ошибка!.")
        return

    num_bins, bins_content = exact_bin_packing(items, bin_capacity)

    if num_bins is None:
        print("Не удалось найти решение.")
        return

    print(f"\nМинимальное количество ящиков: {num_bins}")
    for i, content in enumerate(bins_content):
        print(f"Ящик {i + 1}: {content} (сумма: {sum(content)})")


if __name__ == "__main__":
    main()
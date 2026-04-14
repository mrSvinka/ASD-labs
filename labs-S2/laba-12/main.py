def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w],
                               dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Восстановление выбранных предметов
    w = capacity
    chosen = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen.append(i - 1)  # индекс предмета
            w -= weights[i - 1]

    chosen.reverse()
    return dp[n][capacity], chosen

def main():
    n = int(input("Количество предметов: "))
    weights = []
    values = []
    print("Вес и стоимость (через пробел):")
    for i in range(n):
        w, v = map(int, input(f"Предмет {i}: ").split())
        weights.append(w)
        values.append(v)
    capacity = int(input("Вместимость рюкзака: "))

    max_value, chosen = knapsack(weights, values, capacity)
    print(f"Максимальная стоимость: {max_value}")
    print("Выбранные предметы:", chosen)
    total_weight = sum(weights[i] for i in chosen)
    print(f"Общий вес выбранных предметов: {total_weight}")

if __name__ == "__main__":
    main()

    # 3
    # 2 3
    # 3 4
    # 4 5
    # 5



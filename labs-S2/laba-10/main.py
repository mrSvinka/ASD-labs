def egg_drop(floors=100, eggs=2):
    dp = [[0] * (eggs + 1) for _ in range(floors + 1)]

    # Базовые случаи
    for i in range(1, floors + 1):
        dp[i][1] = i               # одно яйцо – линейный поиск
    for j in range(1, eggs + 1):
        dp[1][j] = 1               # один этаж – один бросок
        dp[0][j] = 0

    for f in range(2, floors + 1):
        for e in range(2, eggs + 1):
            dp[f][e] = float('inf')
            for x in range(1, f + 1):
                worst = 1 + max(dp[x - 1][e - 1], dp[f - x][e])
                dp[f][e] = min(dp[f][e], worst)
    return dp[floors][eggs]


def main():
    floors = 100
    eggs = 2
    result = egg_drop(floors, eggs)
    print(f"Здание: {floors} этажей")
    print(f"Количество яиц: {eggs}")
    print(f"Минимальное количество бросков в худшем случае: {result}")
    # Правильный ответ: 14


if __name__ == "__main__":
    main()
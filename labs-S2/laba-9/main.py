def tsp(dist):
    n = len(dist)
    if n == 0:
        return 0
    INF = float('inf')
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0  # начали в городе 0

    for mask in range(1 << n):
        for u in range(n):
            if dp[mask][u] == INF:
                continue
            for v in range(n):
                if not (mask >> v) & 1:
                    new_mask = mask | (1 << v)
                    dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + dist[u][v])

    full_mask = (1 << n) - 1
    answer = min(dp[full_mask][i] + dist[i][0] for i in range(n))
    return answer


def main():
    # Для 4 городов
    dist_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    print("Матрица расстояний:")
    for row in dist_matrix:
        print(row)
    min_cost = tsp(dist_matrix)
    print(f"\nМинимальная длина маршрута: {min_cost}")


if __name__ == "__main__":
    main()
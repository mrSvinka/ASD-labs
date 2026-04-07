def coin_change_ways(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]
    return dp[amount]


def main():
    test_configs = [
        ([1, 2, 5], 5),
        ([2], 3),
        ([1, 2, 3], 4),
        ([1, 5, 10, 25], 30)
    ]
    for coins, amount in test_configs:
        ways = coin_change_ways(coins, amount)
        print(f"Монеты: {coins}")
        print(f"Сумма: {amount}")
        print(f"Количество способов: {ways}\n")


if __name__ == "__main__":
    main()
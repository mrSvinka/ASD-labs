"""Префикс-функция"""
def prefix_function(s: str) -> list:
    n = len(s)
    pi = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi


"""Z-функция для строки"""
def z_function(s: str) -> list:
    n = len(s)
    z = [0] * n
    l = r = 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z


if __name__ == "__main__":
    s = "ABACABA"
    print(f"Строка: {s}")
    print(f"Префикс-функция: {prefix_function(s)}")
    print(f"Z-функция:       {z_function(s)}")
def rabin_karp_search(text, pattern):
# Возвращает список индексов
    m = len(pattern)
    n = len(text)
    if m == 0 or m > n:
        return []

    # Параметры хеширования
    base = 256  # количество символов в алфавите
    mod = 101   # прос  тое число для уменьшения коллизий

    # хеш образца и первого окна в тексте
    pattern_hash = 0
    window_hash = 0
    h = 1

    for _ in range(m - 1):
        h = (h * base) % mod

    # начальные хеши
    for i in range(m):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % mod
        window_hash = (window_hash * base + ord(text[i])) % mod

    occurrences = []

    for i in range(n - m + 1):
        # Если хеши совпадают, проверяем посимвольно
        if pattern_hash == window_hash:
            if text[i:i + m] == pattern:
                occurrences.append(i)

        # хеш для следующего окна
        if i < n - m:
            # Удаляем левый символ
            window_hash = (window_hash - ord(text[i]) * h) % mod
            # Добавляем правый символ
            window_hash = (window_hash * base + ord(text[i + m])) % mod
            # Приводим к положительному значению
            window_hash = (window_hash + mod) % mod

    return occurrences


if __name__ == "__main__":
    text = "ABAAABCDABABCDABC"
    pattern = "ABC"
    positions = rabin_karp_search(text, pattern)
    print(f"Образец '{pattern}' найден в позициях: {positions}")
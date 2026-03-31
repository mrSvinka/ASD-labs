def boyer_moore_search(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0 or m > n:
        return []

    # Таблица плохих символов
    bad_char = {ch: i for i, ch in enumerate(pattern)}

    # Таблица хороших суффиксов
    def good_suffix_table():
        # массив суффиксов
        suff = [0] * m
        suff[m-1] = m
        g = m-1
        f = 0
        for i in range(m-2, -1, -1):
            if i > g and suff[i + m - 1 - f] < i - g:
                suff[i] = suff[i + m - 1 - f]
            else:
                if i < g:
                    g = i
                f = i
                while g >= 0 and pattern[g] == pattern[g + m - 1 - f]:
                    g -= 1
                suff[i] = f - g

        # Вычисляем сдвиги
        shift = [0] * (m + 1)
        for i in range(m + 1):
            shift[i] = m - suff[0] if i == 0 else m - suff[m - i]
        shift = [m] * (m + 1)
        for i in range(m):
            shift[suff[i]] = min(shift[suff[i]], m - 1 - i)
        for i in range(m-1, -1, -1):
            if shift[i] > m - i:
                shift[i] = shift[i+1] if i+1 <= m else m
        return shift

    gs = good_suffix_table()
    occurrences = []
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            occurrences.append(i)
            i += gs[0]   # сдвиг по хорошему суффиксу
        else:
            bc_shift = j - bad_char.get(text[i + j], -1)
            gs_shift = gs[j + 1] if j + 1 <= m else 1
            i += max(bc_shift, gs_shift)
    return occurrences


if __name__ == "__main__":
    text = "ABAAABCDABABCDABC"
    pattern = "ABC"
    print(boyer_moore_search(text, pattern))
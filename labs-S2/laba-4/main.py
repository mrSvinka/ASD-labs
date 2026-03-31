def compute_prefix_function(pattern): #Вычисляет префикс-функцию для образца.
    m = len(pattern)
    pi = [0] * m  #длина наибольшего собственного префикса
    j = 0  # длина текущего совпадающего префикса
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j
    return pi


def kmp_search(text, pattern):
    if not pattern:
        return []  #нет вхождений

    m = len(pattern)
    pi = compute_prefix_function(pattern)

    occurrences = []
    j = 0  # количество совпавших символов образца
    for i, ch in enumerate(text):
        # Пока не совпадает и j>0, откатываем j по префикс-функции
        while j > 0 and ch != pattern[j]:
            j = pi[j - 1]
        if ch == pattern[j]:
            j += 1
        if j == m:
            occurrences.append(i - m + 1)  # индекс начала вхождения
            j = pi[j - 1]  # поиск перекрывающихся вхождений
    return occurrences


if __name__ == "__main__":
    text = "ABAAABCDABABCDABC"
    pattern = "ABC"
    print(f"Образец '{pattern}' найден в позициях: {kmp_search(text, pattern)}")
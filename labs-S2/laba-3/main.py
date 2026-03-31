def build_automaton(pattern):
    m = len(pattern)
    alphabet = sorted(set(pattern))     # алфавит - уникальные символы
    trans = {}

    # Для каждого состояния q (0..m) и каждого символа c в алфавите
    for q in range(m + 1):
        for c in alphabet:
            # Строка, которая получится, если добавить символ c к уже обработанной части
            k = min(m, q + 1)
            while k > 0:
                if pattern[:k] == (pattern[:q] + c)[-k:]:
                    break
                k -= 1
            trans[(q, c)] = k
    return trans, alphabet


#Ищет все вхождения pattern в text
def search(text, pattern):
    m = len(pattern)
    trans, alphabet = build_automaton(pattern)

    state = 0 #где найден образец
    occurrences = []

    for i, ch in enumerate(text):
        # Если символ не в алфавите, автомат переходит в состояние 0
        if ch in alphabet:
            state = trans[(state, ch)]
        else:
            state = 0

        if state == m:
            occurrences.append(i - m + 1)

    return occurrences


if __name__ == "__main__":
    text = "ABAAABCDABABCDABC"
    pattern = "ABC"
    print(f"Образец '{pattern}' найден в позициях: {search(text, pattern)}")
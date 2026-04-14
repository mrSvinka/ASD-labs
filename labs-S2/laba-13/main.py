def first_fit_decreasing(items, bin_capacity): # Сортируем предметы по убыванию размера
    sorted_items = sorted(items, reverse=True)
    bins = []  # список остаточных вместимостей ящиков
    assignment = [[] for _ in range(len(items))]  # предметы в каждом ящике

    for size in sorted_items:
        placed = False
        for i in range(len(bins)):
            if bins[i] >= size:
                bins[i] -= size
                assignment[i].append(size)
                placed = True
                break
        if not placed:
            bins.append(bin_capacity - size)
            assignment[len(bins)-1].append(size)

    return len(bins), assignment[:len(bins)]

def main():
    n = int(input("Количество предметов: "))
    items = []
    print("Размеры предметов через пробел (в одной строке):")
    items = list(map(int, input().split()))
    if len(items) != n:
        print("Количество предметов не совпадает с введённым числом.")
        items = items[:n]
    bin_capacity = int(input("Вместимость одного ящика: "))

    num_bins, bins_content = first_fit_decreasing(items, bin_capacity)
    print(f"Минимальное количество ящиков (приближённо): {num_bins}")
    print("Распределение предметов по ящикам:")
    for i, content in enumerate(bins_content):
        print(f"Ящик {i+1}: {content} (заполнено: {sum(content)} из {bin_capacity})")

if __name__ == "__main__":
    main()

    # 6
    # 1 - 6
    # 7


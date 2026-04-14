def is_safe(vertex, color, graph, colors, k): #Проверяет, можно ли назначить вершине vertex цвет color при текущей раскраске
    for neighbor in range(len(graph)):
        if graph[vertex][neighbor] == 1 and colors[neighbor] == color:
            return False
    return True


def graph_coloring_util(graph, k, colors, vertex): #Рекурсивная функция backtracking.
    if vertex == len(graph):
        return True

    for color in range(1, k + 1):
        if is_safe(vertex, color, graph, colors, k):
            colors[vertex] = color
            if graph_coloring_util(graph, k, colors, vertex + 1):
                return True
            colors[vertex] = 0  # откат
    return False


def graph_coloring(graph): #Возвращает (минимальное число цветов, массив цветов для каждой вершины).
    n = len(graph)
    colors = [0] * n
    for k in range(1, n + 1):
        if graph_coloring_util(graph, k, colors, 0):
            return k, colors
    return n, list(range(1, n + 1))  # худший случай


def main():
    n = int(input("Количество вершин: "))
    print("Матрицу смежности построчно (0 или 1):")
    graph = []
    for _ in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    min_colors, coloring = graph_coloring(graph)
    print(f"Минимальное количество цветов: {min_colors}")
    print("Раскраска вершин:")
    for i, c in enumerate(coloring):
        print(f"Вершина {i}: цвет {c}")


if __name__ == "__main__":
    main()

#Ввод
    # 4
    # 0 1 0 1
    # 1 0 1 0
    # 0 1 0 1
    # 1 0 1 0






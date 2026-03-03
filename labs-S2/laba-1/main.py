import math
from functools import cmp_to_key


def read_points():
    n = int(input("Ввод количества точек: "))
    points = []
    for i in range(n):
        x, y = map(float, input(f"Ввод координат точки {i+1} (x y): ").split())
        points.append((x, y))
    return points

#сортировка, относительно базовой точски
def polar_angle(p0, p1):
    dx = p1[0] - p0[0]
    dy = p1[1] - p0[1]
    return math.atan2(dy, dx)

#сравнение удалённости при равных углах
def distance_sq(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return dx*dx + dy*dy

#Векторное произведение (oa x ob)
def cross(o, a, b):
    # Отрицательное — правый поворот. Ноль — точки коллинеарны.
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

'''Алгоритм Грэхема'''
def graham_scan(points):
    n = len(points)
    if n < 3:
        return []   #мало точек

    p0 = min(points, key=lambda p: (p[1], p[0])) # Находим первую точку (самую нижнюю левую точку)

    def compare(p1, p2):     # Сортируем все точки по углу, относительно p0.
        ang1 = polar_angle(p0, p1)
        ang2 = polar_angle(p0, p2)
        if ang1 < ang2:
            return -1
        elif ang1 > ang2:
            return 1
        else:
            #Углы равны (сравниваем по расстоянию от p0)
            dist1 = distance_sq(p0, p1)
            dist2 = distance_sq(p0, p2)
            if dist1 < dist2:
                return -1
            elif dist1 > dist2:
                return 1
            else:
                return 0   #точки совпадают

    sorted_points = sorted([p for p in points if p != p0], key=cmp_to_key(compare))     # Список точек без p0

    # 3. Удаление коллинеарных точкек (лежащиих на одном луче из p0)
    unique = [p0]  # начинаем с базовой точки
    for p in sorted_points:

        if len(unique) >= 2: # берем самую дальнюю точку
            if math.isclose(polar_angle(p0, unique[-1]), polar_angle(p0, p), rel_tol=1e-9):
                unique[-1] = p
            else:
                unique.append(p)      # добавляем точку
        else:
            unique.append(p)           #второй точкой идёт первая из списка

    if len(unique) < 3:
        return []

    stack = [unique[0], unique[1], unique[2]] #Строим выпуклую оболочку с помощью стека.

    for i in range(3, len(unique)): # образуют неправильный поворот
        while len(stack) >= 2 and cross(stack[-2], stack[-1], unique[i]) <= 0:
            stack.pop()                # убираем точку, нарушающую выпуклость
        stack.append(unique[i])        # добавляем новую точку

    return stack


def main():
    points = read_points()
    hull = graham_scan(points)

    if not hull:
        if len(points) < 3:
            print("Выпуклая оболочка не существует (точек меньше 3)")
        else:
            print("Выпуклая оболочка не существует (точки коллинеарны)")
    else:
        print("\nВыпуклая оболочка состоит из точек:")
        for i, p in enumerate(hull):
            print(f"{i+1}: ({p[0]:.3f}, {p[1]:.3f})")


if __name__ == "__main__":
    main()
import math
from itertools import combinations

EPS = 1e-12


class Point:
    '''точки на плоскости'''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x:.3f}, {self.y:.3f})"

    def __eq__(self, other):  # погрешность
        return abs(self.x - other.x) < EPS and abs(self.y - other.y) < EPS

    def __hash__(self):  # округление до 6 знаков
        return hash((round(self.x, 6), round(self.y, 6)))


def read_points():
    n = int(input("Ввод количества точек: "))
    points = []
    for i in range(n):
        x, y = map(float, input(f"Ввод координат точки {i + 1} (x y): ").split())
        points.append(Point(x, y))
    return points


# функции
def cross(o, a, b):
    '''Векторное произведение (oa x ob)'''
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)

def dot(a, b):
    '''Скалярное произведение векторов a и b'''
    return a.x * b.x + a.y * b.y

def sub(a, b):
    '''Разность векторов a - b'''
    return Point(a.x - b.x, a.y - b.y)

def add(a, b):
    '''Сумма векторов a + b'''
    return Point(a.x + b.x, a.y + b.y)

def mul(v, k):
    '''Умножение вектора v на скаляр k'''
    return Point(v.x * k, v.y * k)

def length_sq(v):
    '''Квадрат длины вектора'''
    return v.x * v.x + v.y * v.y

def distance(p1, p2):
    '''Расстояние между двумя точками'''
    return math.hypot(p1.x - p2.x, p1.y - p2.y)


# Проверка принадлежности
def point_in_triangle(p, a, b, c):
    # Векторы из вершины a
    v0 = sub(c, a)  # вектор a->c
    v1 = sub(b, a)  # вектор a->b
    v2 = sub(p, a)  # вектор a->p

    # Скалярные произведения
    dot00 = dot(v0, v0)
    dot01 = dot(v0, v1)
    dot02 = dot(v0, v2)
    dot11 = dot(v1, v1)
    dot12 = dot(v1, v2)

    # Вычисление знаменателя
    inv_denom = 1.0 / (dot00 * dot11 - dot01 * dot01)

    u = (dot11 * dot02 - dot01 * dot12) * inv_denom
    v = (dot00 * dot12 - dot01 * dot02) * inv_denom

    # Точка внутри, если u > 0, v > 0 и u + v < 1
    return u > EPS and v > EPS and (u + v) < 1 - EPS


# Проверка
def on_segment(p, a, b):
    # проверяем, что p находится в прямоугольной bounding box отрезка
    return (min(a.x, b.x) - EPS <= p.x <= max(a.x, b.x) + EPS and
            min(a.y, b.y) - EPS <= p.y <= max(a.y, b.y) + EPS and
            abs(cross(a, b, p)) < EPS)


def segments_intersect(a1, a2, b1, b2):  # пересекаются ли отрезки a1a2 и b1b2
    o1 = cross(a1, a2, b1)
    o2 = cross(a1, a2, b2)
    o3 = cross(b1, b2, a1)
    o4 = cross(b1, b2, a2)

    # отрезки пересекаются в одной внутренней точке
    if (o1 > EPS and o2 < -EPS) or (o1 < -EPS and o2 > EPS):
        if (o3 > EPS and o4 < -EPS) or (o3 < -EPS and o4 > EPS):
            return True

    # особый случаи: одна из точек лежит на другом отрезке
    if abs(o1) < EPS and on_segment(b1, a1, a2):
        return True
    if abs(o2) < EPS and on_segment(b2, a1, a2):
        return True
    if abs(o3) < EPS and on_segment(a1, b1, b2):
        return True
    if abs(o4) < EPS and on_segment(a2, b1, b2):
        return True

    return False


# Пересечение прямых
def line_intersection(p1, p2, p3, p4):
    x1, y1 = p1.x, p1.y
    x2, y2 = p2.x, p2.y
    x3, y3 = p3.x, p3.y
    x4, y4 = p4.x, p4.y

    # Определитель системы (направляющие векторы)
    det = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(det) < EPS:
        return None  # прямые параллельны или совпадают

    # Вычисление точки пересечения по формулам Крамера
    x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / det
    y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / det
    return Point(x, y)


# ---Пересечение прямой и отрезка
def line_segment_intersection(line_p1, line_p2, seg_a, seg_b):
    inter = line_intersection(line_p1, line_p2, seg_a, seg_b)
    if inter is None:
        return None
    if on_segment(inter, seg_a, seg_b):
        return inter
    return None


# Пересечение прямой и окружности
def circle_line_intersection(center, r, line_p1, line_p2):
    # Переносим центр окружности в начало координат
    x1 = line_p1.x - center.x
    y1 = line_p1.y - center.y
    x2 = line_p2.x - center.x
    y2 = line_p2.y - center.y

    # Направляющий вектор прямой
    dx = x2 - x1
    dy = y2 - y1

    # Коэффициенты квадратного уравнения
    a = dx * dx + dy * dy
    b = 2 * (x1 * dx + y1 * dy)
    c = x1 * x1 + y1 * y1 - r * r

    # Дискриминант
    disc = b * b - 4 * a * c
    if disc < -EPS:
        return []  # нет пересечений
    if abs(disc) < EPS:
        # Одно касание
        t = -b / (2 * a)
        x = x1 + t * dx
        y = y1 + t * dy
        return [Point(x + center.x, y + center.y)]
    else:
        # Два пересечения
        sqrt_disc = math.sqrt(disc)
        t1 = (-b - sqrt_disc) / (2 * a)
        t2 = (-b + sqrt_disc) / (2 * a)
        p1 = Point(x1 + t1 * dx + center.x, y1 + t1 * dy + center.y)
        p2 = Point(x1 + t2 * dx + center.x, y1 + t2 * dy + center.y)
        return [p1, p2]


# пересечение отрезка и окружности
def circle_segment_intersection(center, r, seg_a, seg_b):
    points = circle_line_intersection(center, r, seg_a, seg_b)
    result = []
    for p in points:
        if on_segment(p, seg_a, seg_b):
            result.append(p)
    return result


# Пересечение двух окружностей
def circle_circle_intersection(c1, r1, c2, r2):
    dx = c2.x - c1.x
    dy = c2.y - c1.y
    d = math.hypot(dx, dy)  # расстояние между центрами

    # Проверка на совпадение окружностей (бесконечно много точек)
    if abs(d) < EPS and abs(r1 - r2) < EPS:
        return []  # для задачи вернём пустой список (неопределённость)

    # Проверка на отсутствие пересечения
    if d > r1 + r2 + EPS or d < abs(r1 - r2) - EPS or d < EPS:
        return []

    # Расстояние от c1 до точки на линии центров
    a = (r1 * r1 - r2 * r2 + d * d) / (2 * d)
    # Высота
    h = math.sqrt(max(0, r1 * r1 - a * a))
    # Точка на линии центров
    x0 = c1.x + a * dx / d
    y0 = c1.y + a * dy / d

    if abs(h) < EPS:
        # Одна точка касания
        return [Point(x0, y0)]

    # Вектор перпендикулярный линии центров
    rx = -dy * (h / d)
    ry = dx * (h / d)

    p1 = Point(x0 + rx, y0 + ry)
    p2 = Point(x0 - rx, y0 - ry)
    return [p1, p2]


# Основная задача: поиск вложенных треугольников
def triangles_from_points(points):
    return list(combinations(points, 3))


def triangles_nested(t1, t2):
    a1, b1, c1 = t1
    a2, b2, c2 = t2

    # Проверка, что все вершины t1 внутри t2
    if not (point_in_triangle(a1, a2, b2, c2) and
            point_in_triangle(b1, a2, b2, c2) and
            point_in_triangle(c1, a2, b2, c2)):
        return False

    # Проверка, что стороны треугольников не пересекаются
    sides1 = [(a1, b1), (b1, c1), (c1, a1)]
    sides2 = [(a2, b2), (b2, c2), (c2, a2)]

    for s1 in sides1:
        for s2 in sides2:
            if segments_intersect(s1[0], s1[1], s2[0], s2[1]):
                return False
    return True


def find_nested_triangles(points):
    triangles = triangles_from_points(points)
    # Перебираем все уникальные пары треугольников
    for i, t1 in enumerate(triangles):
        for t2 in triangles[i + 1:]:
            if triangles_nested(t1, t2):
                return t1, t2
            if triangles_nested(t2, t1):
                return t2, t1
    return None, None


def main():
    points = read_points()
    if len(points) < 6:
        print("Для существования двух различных треугольников нужно не менее 6 точек.")

    inner, outer = find_nested_triangles(points)
    if inner and outer:
        print("\nНайдены треугольники:")
        print(f"Внутренний: {inner[0]}, {inner[1]}, {inner[2]}")
        print(f"Внешний: {outer[0]}, {outer[1]}, {outer[2]}")
    else:
        print("\nВложенных треугольников не найдено.")


if __name__ == "__main__":
    main()
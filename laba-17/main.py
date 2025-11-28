"""
Лаба №17 “Операции над БНП: поиск, добавление, удаление”
Дерево вводится в программу в формате линейно-скобочной записи. Затем появляется меню,
в котором доступна операция добавления, удаления и поиска вершины БДП.
После выполнения операции программа должна возвращаться снова в меню.
При выходе их него до завершения программы на экран должно быть выведено БДН любым способом
(в виде линейно-скобочной записи или в графической форме).
"""

class TreeNode:
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None

##Парсинг строки в бинарное дерево
def parse_tree(s):
    if not s or s == ',':
        return None

    i = 0
    while i < len(s) and s[i] not in '(,)':
        i += 1

    if i == 0:
        return None

    node = TreeNode(int(s[:i]))

    if i < len(s) and s[i] == '(':
        balance = 0
        j = i
        while j < len(s):
            if s[j] == '(':
                balance += 1
            elif s[j] == ')':
                balance -= 1
            elif s[j] == ',' and balance == 1:
                left_str = s[i + 1:j]
                right_str = s[j + 1:len(s) - 1] if s[-1] == ')' else s[j + 1:]

                node.left = parse_tree(left_str)
                node.right = parse_tree(right_str)
                break
            j += 1

    return node

##В линейно-скобочную строку
def tree_to_string(root):
    if not root:
        return ""

    result = str(root.value)

    if root.left or root.right:
        result += "(" + tree_to_string(root.left) + "," + tree_to_string(root.right) + ")"

    return result

##Поиск вершины в БДП
def search_node(root, value):
    if not root:
        return False

    if root.value == value:
        return True
    elif value < root.value:
        return search_node(root.left, value)
    else:
        return search_node(root.right, value)

##Добавление новой вершины в БДП
def insert_node(root, value):
    if not root:
        return TreeNode(value)

    if value < root.value:
        root.left = insert_node(root.left, value)
    elif value > root.value:
        root.right = insert_node(root.right, value)
    ## Если значение уже существует, ничего не делаем

    return root

##Нахождение минимального значения в поддереве
def find_min(node):
    current = node
    while current and current.left:
        current = current.left
    return current

##Удаление вершины из БДП
def delete_node(root, value):
    if not root:
        return root

    # Поиск удаляемого узла
    if value < root.value:
        root.left = delete_node(root.left, value)
    elif value > root.value:
        root.right = delete_node(root.right, value)
    else:
        # Узел найден - обработка трех случаев

        # Случай 1: У узла нет потомков или только один потомок
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        # Случай 2: У узла два потомка
        # Находим минимальный узел в правом поддереве
        temp = find_min(root.right)
        root.value = temp.value
        root.right = delete_node(root.right, temp.value)

    return root

##Меню
def display_menu():
    print("\n" + "-" * 66)
    print("           ВЫБЕРИТЕ ОПЕРАЦИЮ НАД БИНАРНЫМ ДЕРЕВОМ")
    print("-" * 66)
    print("1. Поиск вершины")
    print("2. Добавление вершины")
    print("3. Удаление вершины")
    print("4. Показать текущее дерево")
    print("5. Выход")
    print("_" * 66)

##Ввод начального дерева
def main():
    print("Введите дерево в линейно-скобочной форме:")
    input_string = input("Дерево: ").strip()

    ##Парсинг дерева
    root = parse_tree(input_string)
    print(f"\nНачальное дерево: {tree_to_string(root)}")

    ##Основной цикл
    while True:
        display_menu()
        choice = input("Выберите операцию: ").strip()

        ##Поиск вершины
        if choice == '1':
            try:
                value = int(input("Введите значение для поиска: "))
                if search_node(root, value):
                    print(f"Вершина со значением {value} присутствует")
                else:
                    print(f"Вершина со значением {value} отсутствует")
            except ValueError:
                print("Ошибка: введите целое число")

        ##Добавление вершины
        elif choice == '2':
            try:
                value = int(input("Введите значение для добавления: "))
                root = insert_node(root, value)
                print(f"Вершина {value} добавлена")
                print(f"Текущее дерево: {tree_to_string(root)}")
            except ValueError:
                print("Ошибка: введите целое число")

        ##Удаление вершины
        elif choice == '3':
            try:
                value = int(input("Введите значение для удаления: "))
                if search_node(root, value):
                    root = delete_node(root, value)
                    print(f"Вершина {value} удалена")
                    print(f"Текущее дерево: {tree_to_string(root)}")
                else:
                    print(f" Вершина {value} не найдена")
            except ValueError:
                print("Ошибка: введите целое число")

        ##Показать дерево
        elif choice == '4':
            print(f"\nТекущее дерево: {tree_to_string(root)}")

        ## Выход
        elif choice == '5':
            print("\n" + "-" * 66)
            print("ИТОГОВОЕ ДЕРЕВО:")
            print(f"{tree_to_string(root)}")
            print("Программа открыто возненавидела деревья, и теперь будет плакать в ночи, вспоминая о них...............")
            print("-" * 66)
            break

        else:
            print("Неверный выбор. Выберите от 1 до 5")


##Запуск
if __name__ == "__main__":
    main()

##               8(3(1,6(4,7)),10(,14(13,)))
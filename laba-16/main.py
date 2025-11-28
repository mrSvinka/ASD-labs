"""
Лаба №16 “Не рекурсивный прямой обход” (реализуется с помощью стека).
В качестве выходных данных формируется строка обхода. Например:
Бинарное дерево поиска
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

##Нерекурсивный прямой обход с использованием стека
def iterative_pre_order_traversal(root):
    if not root:
        return []

    result = []
    stack = [root]  ## Инициализируем стек корневым узлом

    while stack:
        ## Извлекаем узел из стека (последний вошел, первый вышел)
        node = stack.pop()
        result.append(node.value)

        ## Сначала добавляем правого потомка, потом левого
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result

## Основная программа
if __name__ == "__main__":
    ## Вход
    input_string = "8(3(1,6(4,7)),10(,14(13,)))"

    root = parse_tree(input_string)

    ## Нерекурсивный прямой обход
    traversal_result = iterative_pre_order_traversal(root)

    result_string = " ".join(map(str, traversal_result))
    print("Нерекурсивный прямой обход:", result_string)
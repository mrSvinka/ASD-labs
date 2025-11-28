"""
Лаба №15 “Рекурсивные обходы (прямой, центральный, концевой)”
"""


class TreeNode:
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None


def parse_tree(s):
    if not s or s == ',':
        return None

    ## Находим корень
    i = 0
    while i < len(s) and s[i] not in '(,)':
        i += 1

    if i == 0:  ## Пустой узел
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

##Прямой обход
def pre_order_traversal(root, result=None):
    if result is None:
        result = []
    if root:
        result.append(root.value)
        pre_order_traversal(root.left, result)
        pre_order_traversal(root.right, result)
    return result

##Центральный обход
def in_order_traversal(root, result=None):
    if result is None:
        result = []
    if root:
        in_order_traversal(root.left, result)
        result.append(root.value)
        in_order_traversal(root.right, result)
    return result

##Концевой обход
def post_order_traversal(root, result=None):
    if result is None:
        result = []
    if root:
        post_order_traversal(root.left, result)
        post_order_traversal(root.right, result)
        result.append(root.value)
    return result


if __name__ == "__main__":
    ## Входная строка
    input_string = "8(3(1,6(4,7)),10(,14(13,)))"
    root = parse_tree(input_string)

    ## Выполняем обходы
    print("Прямой обход:", pre_order_traversal(root))
    print("Центральный обход:", in_order_traversal(root))
    print("Концевой обход:", post_order_traversal(root))
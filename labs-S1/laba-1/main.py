"""
Лаба №1 "Задача о скобках"
(Задача состоит из двух пунктов, но вы можете не париться и делать сразу второй)
На вход подаётся строка, состоящая из скобок. Программа должна определить правильность введённого скобочного выражения.
 Савкин сказал, что программа должна работать на русском языке: "Введите строку", "Строка не существует", "Строка существует" и т.п.
Пункт 1: В строке будут скобки только одного типа: или "()" , или "{}", или "[]"
Пункт 2: В строке будут все три вида скобок
Для успешной сдачи лабы оба пункта программа должна выполнять корректно (можно сделать отдельные программы на каждый пункт)

Пример входа:
()[({}())]
"""



def check_line(s):
    stack = []
    line = {')': '(', ']': '[', '}': '{'}

    #  Какие типы скобок?
    present_line = set()
    for char in s:
        if char in '([{':
            if char == '(':
                present_line.add('round')
            elif char == '[':
                present_line.add('square')
            elif char == '{':
                present_line.add('curly')

    # 1 или 3
    if len(present_line) not in [1, 3]:
        return False

    # Корректность расстановки скобок
    for char in s:
        if char in line.values():  # Кткрывающая скобка
            stack.append(char)
        elif char in line:  # Закрывающая скобка
            if not stack or stack[-1] != line[char]:
                return False
            stack.pop()

    return not stack


def main():
    print("Введите строку из скобок:")
    input_string = input().strip()

    if not input_string:
        print("Строка не существует")
        return

    if check_line(input_string):
        print("Строка существует")
    else:
        print("Строка не существует")

# Точка входа в программу
if __name__ == "__main__":
    main()
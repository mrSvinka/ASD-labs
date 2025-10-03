"""
Лаба №2 "Задача об арифметическом выражении"
На вход подаётся математическое выражение. Элементы - числа. Операции - "+ - * /".
Также есть скобочки. Окончанием выражения служит "=". Программа должна вывести результат выражения

Пример ввода:
2+7*(3/9)-5=

Замечание:
Программа также должна делать "проверку на дурака": нет деления на 0,
 все скобки стоят верно (см лабу №1) и т.п.

"""


def check_brackets(expression):
    """Проверка корректности скобок (как в Лабе №1)"""
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != brackets[char]:
                return False
            stack.pop()

    return len(stack) == 0


def evaluate_expression(expression):
    """Вычисление арифметического выражения"""
    # Удаляем пробелы и проверяем окончание на =
    expression = expression.replace(' ', '')

    if not expression.endswith('='):
        return "Ошибка: выражение должно заканчиваться на '='"

    # Убираем = в конце
    expr = expression[:-1]

    if not expr:
        return "Ошибка: пустое выражение"

    # Проверяем скобки
    if not check_brackets(expr):
        return "Ошибка: неправильные скобки"

    # Проверяем на недопустимые символы
    allowed_chars = set('0123456789.+-*/()[]{}')
    for char in expr:
        if char not in allowed_chars:
            return f"Ошибка: недопустимый символ '{char}'"

    # Алгоритм вычисления с использованием двух стеков
    numbers = []  # стек для чисел
    operators = []  # стек для операторов

    # Приоритеты операций
    priority = {'+': 1, '-': 1, '*': 2, '/': 2}

    def apply_operator(op, a, b):
        """Применяет оператор к двум числам"""
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b == 0:
                raise ZeroDivisionError("Деление на ноль")
            return a / b

    def process_operator():
        """Обрабатывает оператор из стека"""
        if len(numbers) < 2:
            raise ValueError("Недостаточно операндов")
        op = operators.pop()
        b = numbers.pop()
        a = numbers.pop()
        result = apply_operator(op, a, b)
        numbers.append(result)

    i = 0
    n = len(expr)

    while i < n:
        char = expr[i]

        # Обработка чисел
        if char.isdigit() or char == '.':
            j = i
            # Считываем все число
            while j < n and (expr[j].isdigit() or expr[j] == '.'):
                j += 1
            num_str = expr[i:j]

            # Проверяем корректность числа
            if num_str.count('.') > 1:
                return "Ошибка: неправильное число"

            try:
                num = float(num_str) if '.' in num_str else int(num_str)
                numbers.append(num)
            except ValueError:
                return "Ошибка: неправильное число"

            i = j
            continue

        # Обработка открывающих скобок
        elif char in '([{':
            operators.append(char)
            i += 1

        # Обработка закрывающих скобок
        elif char in ')]}':
            opening_bracket = {'}': '{', ']': '[', ')': '('}[char]

            # Выполняем операции пока не дойдем до открывающей скобки
            while operators and operators[-1] != opening_bracket:
                process_operator()

            if not operators:
                return "Ошибка: неправильные скобки"

            # Удаляем открывающую скобку
            operators.pop()
            i += 1

        # Обработка операторов
        elif char in '+-*/':
            # Выполняем операции с более высоким или равным приоритетом
            while (operators and operators[-1] in priority and
                   priority[operators[-1]] >= priority[char]):
                process_operator()

            operators.append(char)
            i += 1

        else:
            return f"Ошибка: недопустимый символ '{char}'"

    # Выполняем оставшиеся операции
    while operators:
        if operators[-1] in '([{':
            return "Ошибка: неправильные скобки"
        process_operator()

    # Проверяем результат
    if len(numbers) != 1:
        return "Ошибка: некорректное выражение"

    result = numbers[0]

    # Если результат целый, возвращаем как int, иначе как float
    if isinstance(result, float) and result.is_integer():
        return int(result)
    return result


def main():
    print("Введите арифметическое выражение (оканчивается на '='):")
    user_input = input().strip()

    if not user_input:
        print("Ошибка: пустой ввод")
        return

    result = evaluate_expression(user_input)

    if isinstance(result, str):
        print(result)
    else:
        print(f"Результат: {result}")


if __name__ == "__main__":
    main()
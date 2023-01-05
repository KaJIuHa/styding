def calculation(operators: tuple, values: tuple):
    op_1, op_2 = operators
    num_1, num_2, num_3 = values

    result = 0

    if op_1 == '+':
        if op_2 == '+':
            result = add(num_1, num_2, num_3)
        elif op_2 == '-':
            temp = add(num_1, num_2)
            result = minus(temp, num_3)
        elif op_2 == '*':
            temp = multi(num_2, num_3)
            result = add(num_1, temp)
        elif op_2 == '/':
            temp = div(num_2, num_3)
            if temp is None:
                return -1
            result = add(num_1, temp)

    if op_1 == '-':
        if op_2 == '+':
            temp = minus(num_1, num_2)
            result = add(temp, num_3)
        elif op_2 == '-':
            result = minus(num_1, num_2, num_3)
        elif op_2 == '*':
            temp = multi(num_2, num_3)
            result = minus(num_1, temp)
        elif op_2 == '/':
            temp = div(num_2, num_3)
            if temp is None:
                return -1
            result = minus(num_1, temp)

    if op_1 == '*':
        if op_2 == '*':
            result = multi(num_1, num_2, num_3)
        elif op_2 == '+':
            temp = multi(num_1, num_2)
            result = add(temp, num_3)
        elif op_2 == '-':
            temp = multi(num_1, num_2)
            result = minus(temp, num_3)
        elif op_2 == '/':
            temp = multi(num_1, num_2)
            if temp is None:
                return -1
            result = div(temp, num_3)

    if op_1 == '/':
        if op_2 == '/':
            result = div(num_1, num_2, num_3)
        elif op_2 == '*':
            temp = div(num_1, num_2)
            result = multi(temp, num_3)
        elif op_2 == '+':
            temp = div(num_1, num_2)
            result = minus(temp, num_3)
        elif op_2 == '-':
            temp = div(num_1, num_2)
            result = minus(temp, num_3)

    print(result)


def add(a, b, c=None):
    if c is None:
        return a + b
    return a + b + c


def minus(a, b, c=None):
    if c is None:
        return a - b
    return a - b - c


def multi(a, b, c=None):
    if c is None:
        return a * b
    return a * b * c


def div(a, b, c=None):
    try:
        if c is None:
            res = a / b
        else:
            res = a / b / c
    except ZeroDivisionError:
        print("Ошибка ввода,на ноль делить нельзя...")
        return None

    else:
        return res


def validate_operators(expression) -> [tuple, bool]:
    """Проверяет корректность операторов"""

    first, second = expression[1], expression[3]
    operators = '+-*/'

    if first in operators and second in operators:
        return first, second
    return False
    # raise TypeError("Введен неккоректный оператор")


def validate_operands(expression) -> [tuple, bool]:
    """Проверяет корректность операндов"""

    try:
        a, b, c = int(expression[0]), int(expression[2]), int(expression[4])
    except ValueError as err:
        print(f"Операнды должны быть положительными однозначными числами\nТип ошибки: {err}")
        return False
    else:
        return a, b, c


def validate(expression: str) -> str:
    """Интерпритация полученного выражения в удобный вид(исключение пробелов)"""

    return expression.replace(" ", "")


def run(example):
    check_opers = validate_operators(validate(example))
    check_nums = validate_operands(validate(example))

    if check_opers and check_nums:
        calculation(check_opers, check_nums)


if __name__ == "__main__":
    print("******Calculator ver. 1.0******")
    while (enter := input("Введите математическое выражение(для выхода оставь пустым): ")):
        run(enter)

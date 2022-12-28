def calculation(expression):
    operator_1, operator_2 = expression[1], expression[3]
    num_1, num_2, num_3 = float(expression[0]), float(expression[2]), float(expression[4])
    if operator_1 == '+' and operator_2 == '+':
        result = add(num_1, num_2, num_3)
        print(result)
    if operator_1 == "+" and operator_2 == "-":
        result = add(num_1, num_2, num_3 * -1)
        print(result)
    if operator_1 == "-" and operator_2 == "-":
        result = minus(num_1, num_2, num_3)
        print(result)
    if operator_1 == "*" and operator_2 == "*":
        result = multi(num_1, num_2, num_3)
        print(result)


def add(a, b, c=0):
    additional = a + b + c
    return additional


def minus(a, b, c=0):
    res = a - b - c
    return res


def multi(a, b, c=0):
    res = a * b * c
    print(res)



def div(a, b, c=0):
    pass


def validate(expression: str) -> str:
    """Интерпритация полученного выражения в удобный вид(исключение пробелов)"""
    expression = expression.replace(" ", "")
    try:
        num_1, num_2, num_3 = float(expression[0]), float(expression[2]), float(expression[4])

    except ValueError:
        print("Введены недопустимые значения")
    return expression


def run(example):
    run_calc = validate(example)
    return run_calc


if __name__ == "__main__":
    enter = input("Введите математическое выражение: ")
    run(enter)


"""
2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
 Дано a, b, c - стороны предполагаемого треугольника.
  Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
  Если хотя бы в одном случае отрезок окажется больше суммы двух других,
   то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""

a = 2
b = 2
c = 2


class ErrorDefault(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(self)

    def __str__(self, string: str = '') -> str:
        return 'Родитель'


class ErrorTriangle(ErrorDefault):
    def __init__(self):
        super().__init__(self)

    def __str__(self) -> str:
        return 'Фигура не является треугольником'


class ErrorNumber(ErrorDefault):
    def __init__(self):
        super().__init__(self)

    def __str__(self) -> str:
        return 'Введенные значения не могут быть меньше 0'




def triangle(a, b, c):
    try:
        a = int(a)

        b = int(b)
        c = int(c)
        if a > 0 and b > 0 and c > 0:
            print('123')
        else:
            print('693')
            raise ErrorNumber
    except ValueError as e:
        print('не числа')

    if (a + b) > c and (b + c) > a and (c + a) > b:
        print("фигура abc является треугольником", end=" ")

        if a == b == c:
            print("равносторонним")
        elif a == b or b == c or c == a:
            print("равнобедренным")

        else:
            print("разносторонним")
    else:
        raise ErrorTriangle


triangle('-2', 1, 2)

"""
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого
треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется
больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
равнобедренным или равносторонним.
"""
while True:
    a = float(input('Определим существование треугольника. Введите сторону a: '))
    b = float(input('Введите сторону b: '))
    c = float(input('Введите сторону c: '))
    if a < 0 or b < 0 or c < 0:
        print('Длины сторон должны быть положительными!')
        continue
    else:
        break

if a > b + c or b > a + c or c > a + b:
    print('Треугольника с такими сторонами не существует')
else:
    if a == b == c:
        print('Равносторонний треугольник')
    elif a == b or a == c or b == c:
        print('Равнобедренный треугольник')
    else:
        print('Разносторонний треугольник')

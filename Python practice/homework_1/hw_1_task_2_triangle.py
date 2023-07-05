# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами
# не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

def check_triangle():
    print('So let us check three numbers to find out if they can make a triangle. '
          'If they can, we will find out whicn triangle they can make. So start!')
    a = ask_for_information('a')
    b = ask_for_information('b')
    c = ask_for_information('c')

    answer = None

    if a <= 0 or b <= 0 or c <= 0 or a + b <= c or b + c <= 0 or c + a <= b:
        answer = "These numbers can't make a triangle..."
    elif a == b == c:
        answer = "These numbers can make a equilateral triangle!"
    elif (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == a**2 + b**2):
        answer = "These numbers can make a right triangle!"
    else:
        answer = "These numbers can make a scalene triangle"
    print(answer)

def ask_for_information(s):
    info_from_user = input(f'Please enter length oh side {s}: ')
    while not info_from_user.isdigit():
        info_from_user = input('Wrong enter. Please enter again: ')
    return float(info_from_user)

check_triangle()
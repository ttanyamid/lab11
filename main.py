a1 = float(input('Введите коэффициент A: '))
b1 = float(input('Введите коэффициент B: '))
c1 = float(input('Введите коэффициент C: '))


def equation(a, b, c):
    if a == 0:
        return 'При первом аргументе ноль невозможен'
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + discr ** 0.5) / (2 * a)
        x2 = (-b - discr ** 0.5) / (2 * a)
        return x1, x2
    elif discr == 0:
        x = -b / (2 * a)
        return x
    else:
        return 'Корней нет'


print('Корни уравнения: ' + str(equation(a1, b1, c1)))
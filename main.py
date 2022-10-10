while True:
    try:
        a = float(input('Введите коэффициент a: '))
        b = float(input('Введите коэффициент b: '))
        c = float(input('Введите коэффициент c: '))
    except Exception:
        print('Введен неверный тип данных(буквы и пустые пробелы использовать нельзя)')
    else:
        discr = b**2 - 4*a*c
        if discr < 0:
            print('Корней нет')
        elif discr == 0:
            x = -b / (2 * a)
            print('x = ' + str(x))
        else:
            x1 = (-b + discr ** 0.5) / (2 * a)
            x2 = (-b - discr ** 0.5) / (2 * a)
            print('x1 = ' + str(x1))
            print('x2 = ' + str(x2))
        break

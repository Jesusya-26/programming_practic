print('Доброго времени суток!\nДанная программа определяет, в какой четверти находится точка, '
      'заданная пользователем по двум координатам x и y.')
try:
    x, y = tuple([float(i) for i in input('Введите два числа (x, y) через пробел: ').split()])
    if x == 0 and y == 0:
        print(f'Точка А({x}, {y}) находится на оси OX (абсцисс) и оси OY (ординат).')
    elif x == 0:
        if y > 0:
            print(f'Точка А({x}, {y}) находится на оси OY (ординат) выше ОХ (абсцисс).')
        else:
            print(f'Точка А({x}, {y}) находится на оси OY (ординат) ниже ОХ (абсцисс).')
    elif y == 0:
        if x > 0:
            print(f'Точка А({x}, {y}) находится на оси OX (абсцисс) справа от OY (ординат).')
        else:
            print(f'Точка А({x}, {y}) находится на оси OX (абсцисс) слева от OY (ординат).')
    else:
        quarters = [x > 0 and y > 0, x < 0 and y > 0, x < 0 and y < 0, x > 0 and y < 0]
        for i in range(len(quarters)):
            if quarters[i]:
                print(f'Точка А({x}, {y}) находится в {i + 1} четверти.')
except Exception:
    print('Некорректный ввод!')

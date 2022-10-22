print('Доброго времени суток!\nДанная программа определяет наибольшее из трёх чисел, введенных пользователем.')

a, b, c = tuple([float(i) for i in input('Введите три числа через пробел: ').split()])
maximum = c
if a > b >= c:
    maximum = a
elif b > c:
    maximum = b
print(f'Наибольшее число: {maximum}')

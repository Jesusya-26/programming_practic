print('Доброго времени суток!\nДанная программа может определить, является ли число, '
      'введенное пользователем, чётным или нет.')

n = float(input("Введите число: "))
if n % 2:
    print(f'Число {n} - нечетное')
else:
    print(f'Число {n} - четное')

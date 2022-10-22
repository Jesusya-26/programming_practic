print('Доброго времени суток!\nДанная программа выводит все простые числа вплоть до заданного.')

try:
    n = int(input('Введите число: '))
    if n < 2:
        raise ValueError
    a = list(range(n + 1))
    res = []

    i = 2
    while i <= n:
        if a[i]:
            res.append(a[i])
            for j in range(i, n + 1, i):
                a[j] = 0
        i += 1
    print(f'Cписок простых чисел в диапазоне от 2 до {n}:\n{", ".join([str(i) for i in res])}')
except Exception:
    print('Некорректный ввод!')

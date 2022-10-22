import sys

print('Доброго времени суток!\nДанная программа определяет, сколько дней осталось до Нового года (2022 год).')
try:
    m, d = tuple([int(i) for i in input('Пожалуйста, введите номер месяца и дня: ').split()])
    if m < 1 or m > 12 or d < 1 or d > 31:
        raise ValueError
    if m == 2 and d > 28:
        raise ValueError
    if m in (4, 6, 9, 11) and d > 30:
        raise ValueError
    if m == 1 and d == 1:
        print('Сегодня Новый год! До следующего 366 дней!')
        sys.exit(0)
    res = 1
    if m == 1:
        res += 31 - d
    elif m == 2:
        res += 28 - d
    elif m in (4, 6, 9, 11):
        res += 30 - d
    else:
        res += 31 - d
    for i in range(m + 1, 13):
        if i in (4, 6, 9, 11):
            res += 30
        elif i == 2:
            res += 28
        else:
            res += 31
    if res % 10 == 1 and res != 11:
        print(f'До Нового года {res} день!')
    elif 1 < res % 10 < 5 and (res < 11 or res > 15):
        print(f'До Нового года {res} дня!')
    elif res % 10 > 4 or 10 < res < 15:
        print(f'До Нового года {res} дней!')
except Exception:
    print('Упс! Некорректно введены данные!')

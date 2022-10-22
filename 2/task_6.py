print('Доброго времени суток!\nДанная программа умеет здороваться с пользователем в '
      'зависимости от введенного времени суток.')
try:
    name, time = tuple([i for i in input('Пожалуйста, введите свое имя и текущее время '
                                         'в формате hh:mm через пробел, например: Руслан 00:00\nВвод: ').split()])
    if len(time) != 5:
        raise Exception
    for i in time.split(':'):
        for j in i:
            if not j.isdigit():
                raise Exception
    if time[0] != '0':
        if int(time[:2]) > 23:
            raise Exception
    if time[3] != '0':
        if int(time[3:]) > 59:
            raise Exception
    if time[0] == '0':
        if 0 <= int(time[1]) < 5:
            print(f'Доброй ночи, {name}!')
        else:
            print(f'Доброе утро, {name}!')
    else:
        if int(time[:2]) > 24:
            raise Exception
        if int(time[:2]) < 12:
            print(f'Доброе утро, {name}!')
        elif 11 < int(time[:2]) < 17:
            print(f'Добрый день, {name}!')
        elif 16 < int(time[:2]) < 22:
            print(f'Добрый вечер, {name}!')
        else:
            print(f'Доброй ночи, {name}!')
except Exception:
    print('Упс! Некорректно введены данные!')

print('Доброго времени суток!\nДанная программа может вывести синтаксически правильную фразу,'
      'используя введённые имя, пол и возраст человека.')
try:
    name, gen, age = tuple([i for i in input('Пожалуйста, введите имя, пол и возраст в следующем формате, например:'
                                             'Руслан мж 18 (или Виолетта ж 18)\nВвод: ').split()])
    if gen == 'мж':
        print(f'Его зовут {name}. Ему {age}', end=' ')
    elif gen == 'ж':
        print(f'Ее зовут {name}. Ей {age}', end=' ')
    else:
        raise ValueError
    if int(age) % 10 == 1 and int(age) != 11:
        print('год.')
    elif 1 < int(age) % 10 < 5 and (int(age) < 11 or int(age) > 15):
        print('года.')
    elif int(age) % 10 > 4 or 10 < int(age) < 15:
        print('лет.')
except Exception:
    print('Упс! Некорректно введены данные!')


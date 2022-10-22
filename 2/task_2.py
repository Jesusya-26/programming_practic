print('Доброго времени суток!\nДанная программа определяет время года по порядковому номеру месяца.')
try:
    n = int(input('Пожалуйста, введите порядковый номер месяца: '))
    if n < 1:
        raise Exception
    n %= 12
    if n < 3:
       print('Бр-рр, холодно! Это зима.')
    elif 2 < n < 6:
        print('Везде слякоть и птицы поют! Это весна.')
    elif 5 < n < 9:
        print('Ну и жара! Это лето.')
    elif n > 8:
        print('Любимое время года Александра Сергеевича! Это осень.')
except Exception:
    print('Усп! Некорректно введены данные!')
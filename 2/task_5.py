print('Доброго времени суток!\nЭто мини-калькулятор, выполняющий простейшие математические операции.')
try:
    nums = [i for i in input('Пожалуйста, введите произвольное количество рациональных чисел через пробел и '
                             'математическую операцию (+, -, *, /, ^) в конце, например: 1.5 2 3 * = 1.5 * 2 * 3 = 9.0'
                             '\nВвод: ').split()]
    res = 0
    if nums[-1] == '+':
        for i in nums[:-1]:
            res += float(i)
    elif nums[-1] == '-':
        res = float(nums[0])
        for i in nums[1:-1]:
            res -= float(i)
    elif nums[-1] == '*':
        res = 1
        for i in nums[:-1]:
            res *= float(i)
    elif nums[-1] == '/':
        res = float(nums[0])
        for i in nums[1:-1]:
            res /= float(i)
    elif nums[-1] == '^':
        res = float(nums[0])
        for i in nums[1:-1]:
            res **= float(i)
    else:
        raise Exception
    print(f"Ответ: {f' {nums[-1]} '.join(nums[:-1])} = {res}")
except Exception:
    print('Упс! Некорректно введены данные!')

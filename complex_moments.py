import os
from collections.abc import Iterable

os.system('COLOR B')


def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    if isinstance(numbers, Iterable):
        for n in numbers:
            try:
                result += n
            except TypeError:
                incorrect_data += 1
                print(f'Некорректный тип данных для подсчёта суммы - {n}')

    return (result, incorrect_data)


def calculate_average(numbers):
    s = personal_sum(numbers)[0]
    m = 0

    try:
        n = len(numbers)
        m = s / n
        return m
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных.')


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать

try:
    os.system('PAUSE')
except:
    os.system('CLS')

def personal_sum(numbers: list = []):
    incorrect_data = 0
    sum = 0
    for i in numbers:
        try:
            sum += i
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - <{i}>, {type(i)}')
            incorrect_data += 1
    return sum, incorrect_data

def calculate_average(numbers: list = []):
    try:
        res = personal_sum(numbers)
        return res[0] / (len(numbers) - res[1])
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None
    except ZeroDivisionError:
        print('Ну на нет и суда нет')
        return 0




print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
print(f'Результат 5: {calculate_average()}') # без параметров
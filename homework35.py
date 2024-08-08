def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) < 2:
        return int(str_number)
    first = int(str_number[:1])
    return first * get_multiplied_digits(int(str_number[1:]))

#def get_multiplied_digits_alternative(number):
#    if number // 10 < 2:
#        return number
#    return (number % 10) * get_multiplied_digits_alternative(number // 10)
# этот вариант нули тоже умножает, то есть результат при 40203 будет 0

result = get_multiplied_digits(40203)
print(result)


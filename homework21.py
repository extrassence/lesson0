first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')
if first == second and first == third and second == third:
    print('Три числа равны')
elif first == second or first == third or second == third:
    print('Два числа равны')
else:
    print('Все числа уникальны')
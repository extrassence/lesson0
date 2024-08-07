def print_params(a=1, b='строка', c=True):
    print(a, b, c)


#1
print_params()
print_params(2, False, 'Другая строка')
print_params(2 == 1, ':-)')
print_params(b=25)
print_params(c=[1, 2, 3])
#2
values_list = [(1, 2), [1, 2], 'Это кортеж и список']
values_dict = {'a': 1, 'b': 'sometimes means'}
#3
values_list_2 = [('Metallica', 1991, 'Track 02'), 'Sad but']
#2
print_params(*values_list)
print_params(**values_dict)
#3
print_params(*values_list_2, False)
# развлекался как мог

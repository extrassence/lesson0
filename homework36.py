def calculate_structure_sum(*params):
    sum=0
    for i in params:
        if isinstance(i, tuple) or isinstance(i, list) or isinstance(i, set):
            sum += calculate_structure_sum(*i)
        elif isinstance(i, str):
            sum += len(i)
        elif isinstance(i, dict):
            for key, value in i.items():
                sum += calculate_structure_sum(key, value)
        else:
            sum += i
    return sum



data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(*data_structure)
print(result)
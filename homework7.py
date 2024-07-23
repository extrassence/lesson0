students = {'Ivanova', 'Znaykina', 'Botanov', 'Petrov', 'Vasechkin', 'Lentyaev', 'Balbesov', 'Sklerozov',
            'Progulshikov'}
grades = [[4, 3, 4, 3, 2, 3], [5, 5, 5, 5, 5, 5, 5], [5, 5, 4, 5, 5, 4], [4, 3, 2, 3, 5, 3, 2], [4, 5, 3, 5, 4],
          [1, 2, 1, 3, 2, 3], [2, 3, 4, 3, 2, 2, 4], [4, 4, 3, 5, 5, 4], [5, 5, 5, 5, 4, 5]]
# пришлось полистать документацию в поисках способа сделать словарь из двух списков
# для удобства восприятия сократил дробную часть до двух цифр
journal = {sorted(list(students))[i]: int(sum(grades[i]) / len(grades[i])*100) / 100 for i in range(len(students))}
print(journal)

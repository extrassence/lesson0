klass = {'Ivanova': 5, 'Znaykina': 5, 'Botanov': 5, 'Petrov': 4, 'Vasechkin': 4, 'Lentyaev': 3, 'Balbesov': 3, 'Sklerozov': 2}
print('Список оценок за домашку:', klass)
print("Оценка лучшего ученика Ботанова:", klass.get('Botanov'))
print("Оценка худшего ученика Прогульщикова:", klass.get('Progulshikov'))
# Ставим Прогульщикову кол, а Склерозов таки сходил и принес домашку, исправляем оценку
klass.update({'Sklerozov': 4, 'Progulshikov': 1})
print('Список оценок за домашку:', klass)
# Исключаем Прогульщикова из школы потому что он совсем не хочет учиться и не ходит на занятия:
print (klass.pop('Progulshikov'))
print('Список оценок за домашку:', klass)

set_grades = set(klass.values())
print('Список оценок класса:', set_grades)
# У Прогульщикова оказалась родственница в отделе образования, поэтому он вернулся вместе с колом
set_grades.add(1)
# Склерозов принес не свою домашку, так что у нас снова есть 2
set_grades.add(2)
# На фоне этих двух идиотов, Лентяев с Балбесовым просто молодцы, ставим им 4, так что троек у нас нет
set_grades.remove(3)
print('Список оценок класса:', set_grades)
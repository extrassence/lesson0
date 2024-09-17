team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 15520.512
team2_time = 21530.31451

timeavg1 = team1_time / (team1_num * score_1)
timeavg2 = team2_time / (team2_num * score_2)

if timeavg2 > timeavg1:
    result = 'Победа команды {}!'.format(team1)
elif timeavg1 > timeavg2:
    result = 'Победа команды {}!'.format(team2)
else:
    result = 'Ничья!'

print('В соревновании участвуют %s и %s!' % (team1, team2))
print('В команде %s %d участников.' % (team1, team1_num))
print('В команде %s %d участников.' % (team2, team2_num))
print('Соревнуются %d против %d!' % (team1_num, team2_num))

print('Команда {} решила {} задач за {} секунд!'.format(team1, score_1, team1_time))
print('Команда {t} решила {s} задач за {tt} секунд!'.format(t=team2, tt=team2_time, s=score_2))

print(f'Команды решили {score_1} и {score_2}, вместе целых {score_1 + score_2} задач!')
print(f'Среднее время решения задач члена команды {team1} = {timeavg1}')
print(f'Среднее время решения задач члена команды {team2} = {timeavg2}')
print(f'Таким образом, результат соревнования - {result} Потому что они работают эффективнее :)')

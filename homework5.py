days_o_week = 0, "Monday", 'Tuesday', 'Wednesday', 4, 'Friday', 'Saturday', 'Sunday'
# В начале 0, чтобы было легче с порядковыми номерами работать
months = [0, 'January', 'February', 'March', 'April', 5, 'June', 'July', 'August', 'September', 'October', 'November', 'December']
print(days_o_week)
print(months)
# days_o_week[4] = 'Thursday' - выдает ошибку потому что это неизменяемый список
months[5] = 'May'
print(days_o_week)
print(months)
days_o_week = days_o_week[0:4] + tuple(['Thursday']) + days_o_week[5:] # если взять лом, можно немного таки изменить
print(days_o_week)
# Всё еще не понимаю, зачем нужны неизменяемые списки. Можно же просто не изменять обычные! Неужели ради памяти?
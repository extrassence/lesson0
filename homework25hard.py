targetcell = int(input ('Введите число ключевой ячейки:'))
passwordcell = ""
for i in range (1, targetcell):
    for j in range (i + 1, targetcell):
        if (i + j) > targetcell:
            break
        if targetcell % (i + j) == 0:
            passwordcell = passwordcell + str(i) + str(j)
print ('Ваш пароль:', passwordcell)

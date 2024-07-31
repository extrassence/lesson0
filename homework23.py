not_primes = list()
primes = list()
last = int(input("До какого числа вести поиск простых чисел? >"))
numbers = range(1, last)
# Если нужно прям из списка, то можно заменить предыдущие две строчки на присвоение numbers списка,
# но поскольку в условном списке были числа от 1 до 15, я подумал, а почему бы и не взять произвольный интервал?
for i in range(len(numbers)):
    for j in range(2, i):
        if numbers[i] % j == 0:
            not_primes.append(numbers[i])
            break
    if not_primes.count(numbers[i]) == 0 and numbers[i] != 1:
        primes.append(numbers[i])
print('Простые числа: ', primes)
print('Составные числа:', not_primes)

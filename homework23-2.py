not_primes = list()
primes = list()
is_not_primes = False
numbers = [991, 992, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 997]
# Жертвуя универсальностью, сделал как просили :) и добавил булеву переменную, вдруг это важно.
for i in numbers:
    for j in range(2, i):
        is_not_primes = i % j == 0
        if is_not_primes:
            not_primes.append(i)
            break
    if not is_not_primes and i != 1:
        primes.append(i)
print('Простые числа: ', primes)
print('Составные числа:', not_primes)

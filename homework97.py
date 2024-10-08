def is_prime(func):
    def wrapper(*args):
        smt = func(*args)
        cnt = 0
        for i in range(2, smt // 2 + 1):
            if smt % i == 0:
                cnt +=1
        if cnt == 0:
            print('Получилось простое число!')
        else:
            print('Простого числа не получилось...')
        return smt
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
def prime(n):
    d = 2
    while d <= n ** 0.5 and n % d != 0:
        d += 1
    return d > n ** 0.5


num = int(input('Введите целое число->'))
for i in range(2, num + 1):
    if prime(i) == 1:
        print(i)

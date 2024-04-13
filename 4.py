x = int(input('Введите целое число->'))
for j in range(1, x + 1):
    summ = 0
    for i in range(1, j + 1):
        summ += i
    print(summ)

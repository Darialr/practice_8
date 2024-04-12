k = 0
summ = 0
income = int(input())
while income != 0:
    summ += income
    k += 1
    income = int(input())
print(summ/k)

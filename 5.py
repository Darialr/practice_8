def perfect_number(number):
    sum_divisors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_divisors += i
    return sum_divisors == number


k = 0
num = int(input("Введите число: "))
for i in range(2, num):
    if perfect_number(i) == 1:
        k += 1
print(k)

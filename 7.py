num = input('Введите число->')
while str.isdigit(num) != 1:
    print('Ошибка. Попробуйте еще раз. ', end="")
    num = input('Введите число->')
print(f'Введено целое число: {num}')

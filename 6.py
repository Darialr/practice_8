x = int(input())
for i in range(1, x + 1):
    spaces = (x - i) * ' '
    asterisks = i * '*'
    print(f'{spaces}{asterisks}')

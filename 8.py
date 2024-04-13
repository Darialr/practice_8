s = '123456789'
for i in s:
    print(f'{s[:int(i)]} * 8 + {i} = {int(s[:int(i)]) * 8 + int(i)}')
print()

for i in s:
    print(f'{s[:int(i)]} * 9 + {i} = {int(s[:int(i)]) * 9 + (int(i) + 1)}')
print()

for i in range(1, 10):
    print(f'{"1" * i} * {"1" * i} = {int("1" * i) * int("1" * i)} ')

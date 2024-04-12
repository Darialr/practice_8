maxi = int(input())
num = int(input())
while num != -1:
    if num > maxi:
        maxi = num
    num = int(input())
print(maxi)

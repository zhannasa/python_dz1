num = int(input('Enter three digit number: '))
sum = 0
while num > 0:
    x = num % 10
    sum = sum + x
    num = num // 10
print(sum)

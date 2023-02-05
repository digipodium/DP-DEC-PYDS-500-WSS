# sum of all digits
num = 4389493239429384
total = 0

while num > 0:
    rem = num % 10
    num = num // 10
    total += rem
    print(rem, num, total)
num = 12345678901
total = 0

while num > 0:
    rem = num % 10
    num = num // 10
    total = total * 10 + rem
print(total)

# hack
num = 12345
rev = str(num)[::-1]
print(rev)

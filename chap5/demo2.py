# Editor : Liquid
# Time :  12:53

# 计算1到100之间的偶数和


sum = 0
a = 1
while a <= 100:
    if a % 2 == 0:
        sum += a
    a += 1

print('1到100之间的偶数和为', sum)

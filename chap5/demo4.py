# Editor : Liquid
# Time :  13:05

# 输出100到999间的水仙花数

'''
水仙花数：153 = 3*3*3+5*5*5+1*1*1
'''

for i in range(100, 1000):
    temp = i
    sum = 0
    while i > 0:
        sum += (i % 10)**3
        i /= 10
        i = int(i)
    if temp == sum:
        print(sum)




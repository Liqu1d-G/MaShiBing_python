# Editor : Liquid
# Time :  13:47

'''
使用嵌套循环
输出一个阶梯型的矩阵
'''

for i in range(9):
    for j in range(i+1):
        print('*', end='\t')  # 不换行输出
    print()  # 打行

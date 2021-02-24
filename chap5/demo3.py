# Editor : Liquid
# Time :  12:59

'''
for-in的语法结构
for 自定义的变量 in 可迭代对象
每一轮循环中，从可迭代对象中取出一个值赋给自定义的变量
'''


for item in 'python':
    print(item)


for item in range(1, 10):
    print(item)


'''若在循环体中不用使用自定义变量，可以将自定义变量写作’_‘'''
for _ in range(3):
    print('人生苦短，我用python')

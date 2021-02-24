import os


# print可以输出数字、字符串


# 可以输出含有字符的表达式
print(3+1)

# 将数据输出到文件中  注意所指定的盘符要存在，并且使用file = fp
fp = open('E:\CODE\python\MaShiBing\chap1\hello.txt', 'a+')
print('hello world', file = fp)
fp.close()


# 不进行换行输出（输出内容在一行中）
print('hello','world')
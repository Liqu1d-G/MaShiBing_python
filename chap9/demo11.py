# Editor : Liquid
# Time :  15:15


# 格式化字符串


#（1） % 占位符
name = '张三'
age = 20
print('我叫%s,今年%d岁' % (name, age))  # 我叫张三,今年20岁

# (2) 使用format方法
print('我叫{0},今年{1}岁'.format(name, age))  # 我叫张三,今年20岁
print('我叫{1},今年{0}岁'.format(name, age))  # 我叫20,今年张三岁


# (3) f-string
print(f'我叫{name},今年{age}岁')  # 我叫张三,今年20岁

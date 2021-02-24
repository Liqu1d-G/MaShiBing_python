# Editor : Liquid
# Time :  14:39

# isidentifier判断是否是合法字符串，即只含有字母数字下划线
s = 'hello,world'

print('1.', s.isidentifier())  # 1. False
print('2.', 'zhangsan'.isidentifier())  # 2. True
print('3.', '张三'.isidentifier())  # 3. True  中文依然算是字母

'''
isspace()判断是否全部由空白字符组成（回车，换行，水平制表）
isalpha（）判断是否全部由字母组成
isdecimal（）判断是否全部由实际值的数字组成
isnumeric()判断是否全部由数字组成
isalnum（）判断是否全部由数字和字母组成
'''
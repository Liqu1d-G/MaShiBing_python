# Editor : Liquid
# Time :  23:03

# 字符串的查询操作

a = 'hello,hello'


print(a.index('lo'))
print(a.find('lo'))  # 3  正向索引


print(a.rindex('lo'))
print(a.rfind('lo'))  # 9 逆向索引

# print(a.index('k'))  # ValueError: substring not found
print(a.find('k'))  # -1


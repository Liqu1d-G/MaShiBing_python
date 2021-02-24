'''
列表中的value，是列表中各个对象的id，列表又有其本身的id和type
列表有两种创建方式
'''

# 列表创建的第一种方式，使用[]

lst = ['hello', 'world', 98]

# 列表创建的第二种方式，使用list函数

lst2 = list(['hello', 'world', 97])

print(lst)
print(lst2)
print(id(lst[0]))
print(id(lst2[0]))

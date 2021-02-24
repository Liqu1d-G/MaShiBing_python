# Editor : Liquid
# Time :  17:59

'''
元组有两种创建方式
一种是使用（）
其实不使用（）也可以，但是如果只有一个元素，一定要使用（）并再元素后加上逗号
另一种是使用内置函数tuple（）
'''

t = ('python', 'world', 98)
print(t)  # ('python', 'world', 98)
print(type(t))  # <class 'tuple'>

t1 = 'python', 'world', 98
print(t1)  # ('python', 'world', 98)
print(type(t1))  # <class 'tuple'>

t2 = tuple(('python', 'world', 98))
print(t2)  # ('python', 'world', 98)

t3 = ('python',)
print(type(t3))  # <class 'tuple'>


# 空列表
lst =[]
lst = list()

# 空字典
d = {}
d = dict()

# 空元组
t = ()
t = tuple()

print(lst)  # []
print(d)  # {}
print(t)  # ()


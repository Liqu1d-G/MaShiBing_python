# Editor : Liquid
# Time :  13:14

# 比较运算符结果为bool类型

a, b = 10, 20
print('a>b?', a > b)
print('a!=b?', a != b)

# ==用于比较对象的value值， is用于比较对象的id标识（地址）
a = b = 10
print(a == b)
print(a is b)
print(a is not b)

# 列表的比较
lst1 = [11, 22, 33, 44]
lst2 = [11, 22, 33, 44]
print(lst2 == lst1)  # True
print(lst2 is lst1)  # False

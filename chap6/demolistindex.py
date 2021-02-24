# Editor : Liquid
# Time :  14:32


list = ['hello', 'world', 98, 'hello']
print(list.index('hello'))  # 如果列表中有相同元素，只返回列表中相同元素的第一个元素的索引
# print(list.index('python'))  # ValueError: 'python' is not in list


# 可以指定区间进行查找

print(list.index('hello', 0, 3))
# print(list.index('hello', 1 ,3))  # ValueError: 'hello' is not in list
print(list.index('hello', 1, 4))
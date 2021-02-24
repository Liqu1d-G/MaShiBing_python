# Editor : Liquid
# Time :  17:11



# 获取字典视图

score = {'张三' : 100, '李四' : 90, '王五': 45}

# 获取所有的key

keys = score.keys()
print(keys)  # dict_keys(['张三', '李四', '王五'])
print(type(keys))  # <class 'dict_keys'>
print(list(keys))  # 将所有key组成的视图转化为列表  ['张三', '李四', '王五']


# 获取所有的value

values = score.values()
print(values)  # dict_values([100, 90, 45])
print(type(values))  # <class 'dict_values'>
print(list(values))  # [100, 90, 45]


# 获取所有的key-value

items = score.items()
print(items)  # dict_items([('张三', 100), ('李四', 90), ('王五', 45)])
print(type(items))  # <class 'dict_items'>
print(list(items))  # [('张三', 100), ('李四', 90), ('王五', 45)]  转换之后的列表元素是元组




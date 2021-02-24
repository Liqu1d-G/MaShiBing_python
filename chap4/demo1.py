# python中一切皆对象，所有对象都有其确定调布尔值
# 测试对象的布尔值

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))  # 空字符串
print(bool(''))  # 空字符串
print(bool([]))  # 空列表
print(bool(list()))  # 空列表
print(bool(()))  # 空元组
print(bool(tuple()))  # 空元组
print(bool({}))  # 空字典
print(bool(dict()))  # 空字典
print(bool(set()))  # 空集合

print('-------其他对象布尔值均为True---------------')

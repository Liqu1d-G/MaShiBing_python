# Editor : Liquid
# Time :  16:06

'''
remove从列表中移除一个元素，如果有重复元素，则移除第一个，若没有该元素，则会报错
pop根据索引移除元素，若不指定索引，则会删除列表中最后一个元素
切片删除至少一个元素
clear清除列表元素
delete删除列表
'''

lst = [10, 20, 30, 40]

lst[1:3] = []  # 切片

print(lst)  # [10, 40]

lst.clear()
print(lst)  # []


del lst  # 删除列表


# Editor : Liquid
# Time :  14:45


lst = [10, 20, 30, 40, 50, 60, 70, 80]

# 列表切片
lst2 = lst[1:6:1]
print(lst2)  # [20, 30, 40, 50, 60]
lst3 = lst[1:6:2]
print(lst3)  # [20, 40, 60]
lst4 = lst[1:6:]
print(lst4)  # [20, 30, 40, 50, 60]  默认步长为1


'''
步长为负数则是逆序输出
不写步长默认为1
不写start和end默认为开始和结尾，负数时相反
切片后形成的是新列表，具有原列表部分映射关系
'''

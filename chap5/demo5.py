# Editor : Liquid
# Time :  13:38

'''
要求输出1到50之间5的倍数
要求使用continue语句
'''


for item in range(1, 51):
    if item%5 != 0:
        continue
    else:
        print(item)

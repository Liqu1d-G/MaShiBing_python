# Editor : Liquid
# Time :  15:14

def fun(num):
    odd = []  # 存奇数
    even = []  # 存偶数
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even


lst = [11, 12, 13, 14, 15]
print(fun(lst))  # ([11, 13, 15], [12, 14])

'''
函数的返回值：
(1)如果函数没有返回值，return可以不写
(2)函数的返回值，如果是一个，直接返回类型
(3)函数的返回值，如果是多个，则返回一个元组

函数在定义是，是否需要返回值，视情况而定
'''

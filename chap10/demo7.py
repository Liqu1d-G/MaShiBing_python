# Editor : Liquid
# Time :  15:36

def fun(a, b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)


lst = [11, 13, 14]
# fun(lst)  # TypeError: fun() missing 2 required positional arguments: 'b' and 'c'
fun(*lst)  # 在函数调用时，将列表中每个元素都转换成位置实参输入

print('------------------------------')
dic = {'a': 111, 'b': 222, 'c': 333}
# fun(dic)  # TypeError: fun() missing 2 required positional arguments: 'b' and 'c'
fun(**dic)  # 在函数调用时，将字典中每个元素都转换成关键字实参输入

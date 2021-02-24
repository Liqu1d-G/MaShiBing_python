# Editor : Liquid
# Time :  15:22

def fun(*args):  # 函数定义时，无法确定实参的个数，使用可变的位置参数
    print(args)


fun(10)  # (10,)
fun(10, 30)  # (10, 30)  以元组的形式传入


def fun1(**args):
    print(args)


fun1(a=10)  # {'a': 10}
fun1(a=10, b=20)  # {'a': 10, 'b': 20}  以字典的形式传入

'''
def fun2(*a,*b):
    pass
    
def fun3(**a,**b):
    pass
    
以上代码会报错
个数可变的位置参数只能有一个
个数可变的关键字参数也只能有一个
'''


def fun4(*args1, **args2):
    pass

'''
def fun5(**args1, args2):
    pass
    
在一个函数的定义过程中，可以同时有可变的位置参数和可变的关键字参数，但是位置参数只能放在关键字参数之前
'''

# print(dir(object))
class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name):
        self.name = name

# 创建C类对象


x = C('Jack')
print(x.__dict__)
print(C.__dict__)
print("--------------------")
print(x.__class__)  # 输出对象所属的类
print(C.__bases__)  # 输出C类的父类


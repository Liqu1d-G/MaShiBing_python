class Student:
    native_pace = '吉林'  # 直接写在类里的变量，称为类属性

    def __init__(self, name, age):
        self.name = name  # self.name称为实体属性，进行了一个赋值的操作，将局部变量name的值赋给了实体属性
        self.age = age

    def eat(self):  # 实例方法
        print("学生在吃饭。。。")

    @staticmethod  # 静态方法
    def method():
        print("我使用了staticmethod进行修饰，所以我是静态方法")

    @classmethod  # 类方法
    def cm(cls):
        print("我使用了classmethod进行修饰，所以我是类方法")


# 在类之外定义的称为函数，在类之内定义的称为方法

def drink():
    print("喝水")

# 类属性的使用方式


print(Student.native_pace)

stu1 = Student('张三', 20)
stu2 = Student('李四', 30)
print(stu1.native_pace)
print(stu2.native_pace)
Student.native_pace = '天津'
print(stu1.native_pace)
print(stu2.native_pace)
print('-----类方法使用方式------')
Student.cm()
print('-----静态方法使用方式------')
Student.method()

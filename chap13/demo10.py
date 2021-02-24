class Person:
    def __init__(self, name, age):
        print('init被调用执行了，self的id值为{0}'.format(id(self)))
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        print('new被调用执行了，cls的id值为{0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('创建的对象的id为：{0}'.format(id(obj)))
        return obj


print("object这个类对象的id为:{0}".format(id(object)))
print("Person这个类对象的id为:{0}".format(id(Person)))

# 创建Person类的实例对象
p1 = Person('张三', 20)
print('p1这个Person类的实例对象的id为：{0}'.format(id(p1)))

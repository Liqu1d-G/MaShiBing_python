# 继承的代码实现


class Person(object):
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def info(self):
        print('姓名：{0}， 年龄：{1}'.format(self.name, self.age))

# 定义子类


class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score

# 测试


stu = Student('Jack', 20, '1001')
stu.info()

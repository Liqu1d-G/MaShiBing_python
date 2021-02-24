class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'my name is {0},i am {1} year old'.format(self.name, self.age)


stu = Student('Jack', 20)
print(dir(stu))
print(stu) # 默认调用__str___()这样的方法
print(type(stu))

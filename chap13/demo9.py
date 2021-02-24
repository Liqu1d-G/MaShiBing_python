class Student(object):
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.name+other.name


stu1 = Student("张三")
stu2 = Student("李四")

s = stu1+stu2
print(s)

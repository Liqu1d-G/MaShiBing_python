class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 年龄不希望再类的外部被使用，所以加了两个_

    def show(self):
        print(self.name, self.__age)


stu = Student('张三', 20)
stu.show()

# 在类的外部使用name与age

print(stu.name)
# print(stu.__age)
print(dir(stu))
print(stu._Student__age)  # 在类的外部可以通过_Student__age访问

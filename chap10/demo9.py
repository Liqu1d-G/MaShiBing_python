# Editor : Liquid
# Time :  15:50


def fun():
    global age
    age = 20
    print(age)


fun()
print(age)  # 20 局部变量如果使用了global声明，其实就是全局变量

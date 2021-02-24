# Editor : Liquid
# Time :  16:13

try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    result = a/b
    print(result)
except ZeroDivisionError:  # except后接错误类型
    print('除数不能为0')
except ValueError:
    print('只能输入数字')
except BaseException as e:
    print(e)
print('程序结束！')

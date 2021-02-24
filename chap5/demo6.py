# Editor : Liquid
# Time :  13:42


# else与循环结构搭配使用
# 若循环全部执行完成，即没有遇到break，则则执行循环对应的else

for item in range(3):
    pwd = input('请输入密码：')
    if pwd == '8888':
        print('密码正确！')
        break
    else:
        print('密码错误')
else:
    print('对不起，三次密码均错误!')

import os

filename = 'student_myself.txt'


def main():
    while True:
        menu()
        choice = input('请选择：')
        if choice == 0:
            print('感谢您的使用！！！')
            break
        if choice == 1:
            insert()
        elif choice == 2:
            search()
        elif choice == 3:
            delete()
        elif choice == 4:
            modify()
        elif choice == 5:
            sort()
        elif choice == 6:
            total()
        elif choice == 7:
            show()
        else:
            print('输入错误请重新输入！！！')
        answer = input('是否回到菜单？y/n')
        while answer != 'y':
            answer = input('是否回到菜单?y/n')
        break


def menu():
    print('=======================学生信息管理系统======================')
    print('\n')
    print('-------------------------功能菜单--------------------------')
    print('\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t5.排序')
    print('\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t0.退出')
    print('----------------------------------------------------------')


def insert():
    student_list = []
    id = input('请输入学生ID：')



def search():
    pass


def delete():
    pass


def modify():
    pass


def sort():
    pass


def total():
    pass


def show():
    pass

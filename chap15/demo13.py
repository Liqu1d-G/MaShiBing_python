class MyContentMgr(object):
    def __enter__(self):
        print('enter方法被调用了')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用了')

    def show(self):
        print('show方法被调用了')


'''
    存在enter和exit方法的类，称为该类对象遵守上下文管理器协议，
    该类对象的实例对象称为上下文管理器
'''

with MyContentMgr() as file:  # 相当于file=MyContentMgr
    file.show()

# Editor : Liquid
# Time :  16:58

'''
获取字典中的元素
第一种方式，使用[]，若键不存在，则会报错keyerror
第二种方式，使用字典的方法get，如果键不存在，会返回一个None
'''

score = {'张三' : 100, '李四' : 90, '王五': 45}

print(score['张三'])
print(score.get('张三'))

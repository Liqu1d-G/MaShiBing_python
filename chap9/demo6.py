# Editor : Liquid
# Time :  14:31


'''
splite()从字符串左边开始切分，默认切分字符为空格，返回列表
可以通过参数sep指定劈分符
通过maxsplie指定最大劈分次数

rsplte（）从右边开始
'''


s = 'hello world python'

lst = s.split()
print(lst)  # ['hello', 'world', 'python']

s1 = 'hello|world|python'
lst1 = s1.split(sep='|')
print(lst1)  # ['hello', 'world', 'python']

lst2 = s1.split(sep='|', maxsplit=1)
print(lst2)  # ['hello', 'world|python']

lst3 = s1.rsplit(sep='|', maxsplit=1)
print(lst3)  # ['hello|world', 'python']

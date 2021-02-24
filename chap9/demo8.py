# Editor : Liquid
# Time :  14:47


s = 'hello,python'
print(s.replace('python', 'java'))  # hello,java 第一个参数表示要替换的字符串，第二个参数表示替换后的字符串

s1 = 'hello,python,python,python'
print(s1.replace('python', 'java', 2))  # hello,java,java,python 第三个参数在有多个相同字符串时表示替换次数

# join将列表和元组中的字符串连接起来，前提是列表和元组的元素全部为字符串
lst = ['hello', 'java', 'python']
print('|'.join(lst))  # hello|java|python
print(''.join(lst))  # hellojavapython
# lst1 = ['hello', 34, 'world']
# print(''.join(lst1))  # TypeError: sequence item 1: expected str instance, int found
print('*'.join('python'))  # p*y*t*h*o*n

# 原字符，不希望转义字符起作用，在字符串前加上r或R
print(r'hello\nworld')
# 注意，最后一个字符不能是反斜杠,但可以是两个反斜杠
print(r'hello,world\\')
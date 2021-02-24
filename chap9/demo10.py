# Editor : Liquid
# Time :  15:04

s = 'hello,python'
s1 = s[:5]  # 由于没有指定开始位置，从开头开始切,切到end前一个
s2 = s[6:]  # 由于没有指定结束位置，从start开始切，切到尾部
print(s1+'!'+s2)  # hello!python

print('---------------------切片[start:end:step]')
print(s[1:5:1])  # ello
print(s[1:8:2])  # el,y
print(s[1:9:2])  # el,y  若超出end则忽略
print(s[1:13:1])  # ello,python  若end大于长度则多余的忽略
print(s[::2])  # hlopto
print(s[::-1])  # nohtyp,olleh  step为负数则逆向输出
print(s[-6::1])  # python

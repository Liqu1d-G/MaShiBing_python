# Editor : Liquid
# Time :  12:29


s = 'hello,python'
print(s.center(20, '*'))  # ****hello,python****  居中对齐，第一个参数为宽度，第二个参数为填充符
print(s.ljust(20, '*'))  # hello,python********  左对齐
print(s.rjust(20, '*'))  # ********hello,python  右对齐
print(s.zfill(20))  # 00000000hello,python  右对齐，用0填充

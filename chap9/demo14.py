# Editor : Liquid
# Time :  15:27

s = '天涯共此时'
# 编码
print(s.encode(encoding='GBK'))  # b'\xcc\xec\xd1\xc4\xb9\xb2\xb4\xcb\xca\xb1'  在GBK这种编码方式中每一个中文占两个字节
print(s.encode(encoding='utf-8'))  # b'\xe5\xa4\xa9\xe6\xb6\xaf\xe5\x85\xb1\xe6\xad\xa4\xe6\x97\xb6'  一个中文占三个字节

# 解码
byte = s.encode(encoding='GBK')  # byte代表一个二级制数据（字节类型的数据）
print(byte.decode(encoding='GBK'))  # 天涯共此时
# print(byte.decode(exec('utf-8')))  # NameError: name 'utf' is not defined


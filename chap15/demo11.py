file = open('d.txt', 'a')

file.write('hello')
file.flush()  # 将缓冲区内容写入文件，但不关闭文件
file.write('world')
file.close()  # 将缓冲区内容写入文件，并关闭文件

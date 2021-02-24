file = open('a.txt', 'r')

file.seek(4)
print(file.read())
print(file.tell())
file.close()

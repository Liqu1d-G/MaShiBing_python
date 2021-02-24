file = open('d.txt', 'a')

file.write('hello')
file.flush()
file.write('world')
file.close()

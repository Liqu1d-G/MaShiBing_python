scr_file = open('photo.jpg', 'rb')

target_file = open('copyphoto.jpg', 'wb')

target_file.write(scr_file.read())

target_file.close()
scr_file.close()

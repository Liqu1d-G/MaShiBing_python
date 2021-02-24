with open('photo.jpg', 'rb') as src_file:
    with open('copyphoto2.jpg', 'wb') as target_file:
        target_file.write(src_file.read())

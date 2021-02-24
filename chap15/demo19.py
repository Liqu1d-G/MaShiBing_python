import os
path = os.getcwd()
lst_files = os.walk(path)
print(lst_files)
for dirpath,dirname,dirfilename in lst_files:

    print(dirpath)
    print(dirname)
    print(dirfilename)
    print('-----------')
    '''
    for dir in dirname:
        print(os.path.join(dirpath, dir))
    for file in dirfilename:
        print(os.path.join(dirpath, file))
    print('-----------------')
    '''
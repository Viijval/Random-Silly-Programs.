import os
parent_dir=input('Enter Parent Directory')
directory=input('Enter New Folder Name')
amt=int(input('Enter amount of folders'))
# a single \ is used as an escape sequence for new line tab etc hence \\, it considers it as a single
exception=['',' ','/',r'\\',':','*','?','|','<','>']
if directory in exception:
    directory='New Folder'
path=os.path.join(parent_dir,directory)
print(path)
try:
    if os.path.exists(path):
        count=1
        while True:
            new_path=path+str(count)
            if not os.path.exists(new_path):
                break
            count+=1
        path=new_path
    for i in range(amt):
        L_path=path+' '+str(i+1)
        os.mkdir(L_path)
except OSError as error:
    print(error)

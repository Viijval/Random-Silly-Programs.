import os
folder=os.listdir(r'E:\V\Editing\Music')
c='cover'
for i in folder:
    dist=i.split()
    if c in dist:
        print('copy')

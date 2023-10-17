"""
import os

#folder path input

path = os.path.abspath(input("C:\\Program Files\\Microsoft SQL Server"))

#for storing size of each
#file
size=0
max_size="C:\\Program Files\\Microsoft SQL Server"
for folder,subfolders,files in os.walk("C:\\Program Files\\Microsoft SQL Server"):
    for file in files:
        size = os.stat(os.path.join(folder,file)).st_size
        if size>max_size:
            max_size = size
            max_file = os.path.join(foldr,file)
print("the largest file is: "+max_size)
print('Size: '+str(max_size)+ 'bytes')

"""

import os
root = "demo"
path = "C:\\Program Files\\Microsoft SQL Server"
root = os.path.abspath(root) 

def test(path):
    big_files = []
    all_paths = [x[0] for x in os.walk(path)]

    for paths in all_paths:

        f_list = filter(os.path.isfile, os.listdir(paths))
        if len(f_list) > 0:
            big_files.append((paths,max(f_list,key=os.path.getsize)))
    return big_files
print ("test(root)")

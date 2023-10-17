
import os

target="C:\\Program Files\\Microsoft SQL Server"

for root, dirnames, files in os.walk(target):
    for x in files:
        if x.endswith('.dll'):
          #print(root + '\\' + x)


import os

path="C:\\Program Files\\Microsoft SQL Server"

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("C:\\Program Files\\Microsoft SQL Server"):
    path = root.split(os.sep)
    print((len(path) - 1) * '---' , os.path.basename(root))
    for file in files:
     # print(len(path) * '---' , file)
    

import os

target="C:\\Program Files\\Microsoft SQL Server"

for root, dirnames, files in os.walk(target):
    for x in files:
        if x.endswith('.exe'):
         # print(root + '\\' + x)


import os
import datetime

def ts_to_dt(ts):
    return datetime.datetime.fromtimestamp(ts)
for item in os.scandir ("C:\\Program Files\\Microsoft SQL Server"):
    # print(item.name, item.path, item.stat().st_size, ts_to_dt(item.stat().st_atime))
     print(item.name, item.path, item.stat().st_size, ts_to_dt(item.stat().st_atime))

"""
import os 
import time 
x=os.stat("C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\Binn\\DatabaseMailprotocols.dll")
Result=(time.time()-x.st_mtime) 
print("The age of the given file is: ",Result)



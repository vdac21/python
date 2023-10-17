import os

path="C:\\Program Files\\Microsoft SQL Server"
pathname="C:\\Program Files\\Microsoft SQL Server"

def recursive_walk(path):
    for folderName, subpaths, filenames in os.walk(path):
        if subpaths:
            for path in paths:
                recursive_walk(subpath)
        print('\npath:pathname' + '\n')
        for filename in filenames:
            print(filename + '\n')
      return r
r=recursive_walk('/name/of/path')
      
 print(r)

import os
x=os.path.exists("C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\\COPY")
print(x)

path="C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\\TEST"
def folder_size(path):
    total = 0
    for entry in os.scandir(path):
        if entry.is_file():
            total += entry.stat().st_size
        elif entry.is_dir():
            total += folder_size(entry.path)
    return total
print(folder_size(path))


import os
 
# assign size
size = 0
 
# assign folder path
Folderpath = 'C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\\TEST'  
 
# get size
for ele in os.scandir(Folderpath):
    size+=os.stat(ele).st_size
     
print(size)


import os
folder='C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\\TEST'
def getFolderSize(folder):
    total_size = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += getFolderSize(itempath)
    return total_size

print ("Size: " + str(getFolderSize(".")))

directory='C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\\TEST'
def get_directory_size(directory):
    """Returns the `directory` size in bytes."""
    total = 0
    try:
        # print("[+] Getting the size of", directory)
        for entry in os.scandir(directory):
            if entry.is_file():
                # if it's a file, use stat() function
                total += entry.stat().st_size
            elif entry.is_dir():
                # if it's a directory, recursively call this function
                try:
                    total += get_directory_size(entry.path)
                except FileNotFoundError:
                    pass
  
                return total
print('directory')

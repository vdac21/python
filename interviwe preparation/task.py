"""
import os
 
# importing shutil module
import shutil
 
# path
path = "C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\\TEST"   
 
# List files and directories
# in '/home/User/Documents'
print("Before copying file:")
print(os.listdir(path))
 
 
# Source path
source = "C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\\TEST"   
 
# Destination path
destination = "C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\\TEST2"   
 
# Copy the content of
# source to destination
dest = shutil.copyfile(source, destination)
 
# List files and directories
# in "/home / User / Documents"
print("After copying file:")
print(os.listdir(path))
 
# Print path of newly
# created file
print("Destination path:", dest)


import os

file_path ='C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\\COPY'
print(os.stat(file_path.st_size))
"""

import os.path

# file to check
file_path = r'C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\\COPY'

sz = os.path.getsize(file_path)
print(f'The {file_path} size is', sz, 'bytes')

import os

file_name = "C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\TEST"

file_stats = os.stat(file_name)

print(file_stats)
print(f'File Size in Bytes is {file_stats.st_size}')
print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}')

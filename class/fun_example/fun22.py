

import time
f = open('app.log', 'r')
#text = f.read() returns entire data from the file as a string 
lines = f.readlines() # returns entire data from the file as a list
f.close()

#lines = text.split('\n')


for line in lines:
    if 'original priority' in line and 'new priority'  in line:
        print(line)

# Count all .py file form the path below

import subprocess
import time

path = "C:\\Users\\91998\\Desktop\\rm2022H2"
cmd = f'dir {path}'

#print(cmd)

resp = subprocess.check_output(cmd, shell=True)

#print(type(resp)) # bytes


resp = resp.decode('utf-8')


#print(type(resp))

lines = resp.split("\n")[7:]



for line in lines:
    #time.sleep(2)
    words = line.split()
    word = words[len(words)-1]
    if '.py' in word:
        print(word)



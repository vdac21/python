import os

run_path = "C:\\Program Files\\Microsoft SQL Server"
exe= input('.exe')
file = open('output.txt', 'w')

for x in os.listdir(run_path):
    file.write(x +'\n')

file.close()
'''
for x in os.listdir(run_path):
    if x.endswith(exe):
        print(x)
        
'''

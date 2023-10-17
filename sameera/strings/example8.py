#python program to convert uppercase to lower case


string=input("enter a string: ")
res=" "
for i in range(len(string)):
    if (string[i]>='A' and string[i]<='Z'):
        res=res+chr(ord(string[i])+32)

print(res)

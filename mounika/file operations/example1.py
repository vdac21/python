fobj=open("C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\\vedhu.txt",'r')
text=fobj.read()
fobj.close()
print(type(text))
print("------------------")
print(text)


#wriring data inside a file
#open

f=open("C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\\vedhu.txt",'w')
f.write("hello")
f.close()

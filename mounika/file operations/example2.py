f=open("C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\\vedhu.txt",'w')
#opening same file
#write
f.write("\n writing new line")
f.close()


"""
when we are opening a file in write mode,if the file is not exist

then it will new create a new file

incase if the file is exist it will over write the content



If you wanted add new content then we need open in append mode

"""

f=open("C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\\vedhu.txt",'a')

f.write("\n-----beautiful flower")
f.close()





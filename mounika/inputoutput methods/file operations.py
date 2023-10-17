#Reading data from the file
#open-->read-->close

#To open
"""
To open a file we have function defined i.e)open()

The open function will take two params 1.filepath ,2.mode
<fileobject>open(filepath,mode)

where the filepath is the location of the file in your system and its strings


"c:\\abc.txt"
"c:\\desktop\\info.txt"


"C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\\vedhu.txt"

where the mode parameter can be either r,w,a

r---reading
w---writing
a---append

the open()function will return the file object

"""
#to read
"""
To read the data from the file we have function called read() function
The read function returns data from the file as a string type
"""


#To close
"""
to close the file we have a function called close()
"""

#open
fobj=open("C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\\vedhu.txt",'r')
text=fobj.read()
fobj.close()
print (type(text))

print("------")
print(text)

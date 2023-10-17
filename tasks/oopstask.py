
class FileController:

    def __init__(self,path,filename):
       self.path=path
       self.filename=filename

    def file_write(self):
        f=open(self.path+'\\'+self.filename,'w')
        text=f.write("mother is first guru")
        f.close()
        #print(f"writing in file:{text}")
    def file_append(self):
        f=open(self.path+'\\'+self.filename,'a')
        data1=f.write("teacher is important for childern life they have teach all things")
        f.close()
        # print(f"append the file:{data1}")
    def file_read(self):
        f=open(self.path+'\\'+self.filename,'r')
        read=f.read()
        f.close()
        print(f"read the file:{read}")
s1=FileController("C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\\practing", "faith.txt")

s1.file_write()
s1.file_append()
s1.file_read()

s2 = FileController("C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\\practing", "faith.txt")

s2.file_write()
s2.file_append()
s2.file_read()

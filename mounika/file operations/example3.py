#WAP read the data from the file vedhu.txt and count the number of words

#step1:Read the data from the file

f=open("C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\\vedhu.txt",'r')
data=f.read()
f.close()
print(data)
#step2:Get the words

words=data.split(' ')
print(words)

#step3:count the words
count=len(words)
print(count)


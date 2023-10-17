#WAP read the data from the file vedhu.txt and count all the words which are starts with b



import time


f=open("C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\\vedhu.txt",'r')
data=f.read()
f.close()
print(data)


words=data.split(' ')
print(words)


bwords=[]
for word in words:
    time.sleep(2)
    print(word)
    if word[0]=='b' or word[0]=='b':
        bwords.append(word)
        print(words)
        print(f"the count the bwords:{len(bwords)} and Total:{len(words)}")

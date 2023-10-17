# WAP read the data from the file sample2.txt and count the number of words


#Step1: Read the data from the file
f = open('C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\\vedhu.txt', 'r')
data = f.read()
f.close()
print(data)

#Step2: Get the words

words = data.split(' ')
print(words)
#Step3: Count the words
count = len(words)
print(count)


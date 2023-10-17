# WAP read the data from the file sample2.txt and

#count all the words which are starts with P
import time


# step1: read the data from the file
f = open("C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\\vedhu.txt", 'r')
text = f.read()
f.close()
print(text)

# step2: Get all the words
words = text.split() # by default it will take space str.split(' ') == str.split()
print(words)

# step3 : Filter out the words starts with P by traversing all the words
Wwords = []
for word in words:
    time.sleep(2)
    print(word)
    if word[0] == 'W' or word[0] == 'W':
        Wwords.append(word)

print(Wwords)
print(f"The count of Wwords: {len(Wwords)} and Total: {len(words)}")

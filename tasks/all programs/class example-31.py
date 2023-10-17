# WAP read the data from the file sample2.txt and

#count all the words which are starts with P
import time


# step1: read the data from the file
f = open('sample2.txt', 'r')
text = f.read()
f.close()
#print(text)

# step2: Get all the words
words = text.split() # by default it will take space str.split(' ') == str.split()
#print(words)

# step3 : Filter out the words starts with P by traversing all the words
pwords = []
for word in words:
    #time.sleep(2)
    #print(word)
    if word[0] == 'P' or word[0] == 'p':
        pwords.append(word)

print(pwords)
print(f"The counrt of Pwords: {len(pwords)} and Total: {len(words)}")


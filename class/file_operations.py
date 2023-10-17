# Requirement 
"""
Read the data from the file app_log.txt file and the count the words
which are starts with s

Read the data from the file app_trace.txt and count the words which are starts
with m

"""
# The code is repeating 


# Read the data from the file - one file 
f = open('app_log.txt', 'r')
text = f.read()
f.close()

# Filtering the words - starts s
words = text.split()
output = []
for word in words:
    word = word.lower()
    if word[0] == 's':
        output.append(word)
print(output)


# Read the data from the file  - another 
f = open('app_trace.txt', 'r')
text = f.read()
f.close()

# Filtering wors  - starts with m 
words = text.split()
output = []
for word in words:
    word = word.lower()
    if word[0] == 'm':
        output.append(word)
print(output)




        
        

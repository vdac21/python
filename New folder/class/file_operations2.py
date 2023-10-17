# Requirement 
"""
Read the data from the file app_log.txt file and the count the words
which are starts with s

Read the data from the file app_trace.txt and count the words which are starts
with m

"""
# The code is repeating 


def file_read(filepath):
    f = open(filepath, 'r')
    text = f.read()
    f.close()
    return text

# Filtering the words - starts s
def filter_wrords(text, ch):
    words = text.split()
    output = []
    for word in words:
        word = word.lower()
        if word[0] == ch:   #'s:
            output.append(word)
    return (output)

t1 = file_read('app_log.txt')
print(filter_wrords(t1, 's'))
print("-----------------------------------")

t2 = file_read('app_trace.txt')
print(filter_wrords(t2, 'm'))

        
        

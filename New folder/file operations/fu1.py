f = open('memory.txt', 'r')
text = f.read()
f.close()
print(text)
words=text.split('\n')
print(words)
for i in words:
    if 'u' in i and 's' in i:
        print(i)

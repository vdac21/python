#the given string contains both lowercase and uppercase letters in random order and combines all lowercase letters and displays in output.
#input:AmaZOn
#output:man
'''
word= "AmaZOn"
output=""
for ch in word:
    if ch>='a' and ch<='z':
        output=output+ch

print(output)
'''

word= "AmaZOn"
output=""
for ch in word:
    if ord(ch)>=97 and ord(ch)<=122:
        output=output+ch

print(output)

"""
The given string contains both lowercase and
uppercase letters in random order and combines all lowercase letters and displays in output.
Example:  #input :   AmaZOn
	    #output: man

"""

#Note:  When the output is a string , define a empty to string
#       to store the output

# Solution-1
word = "AmaZOn"
output= ""
for ch in word:
    if ch >= 'a' and ch <= 'z':
        output = output + ch

print(output)


#Solution-2   
word = "AmaZOn"
output= ""
for ch in word:
    if ord(ch) >= 97 and ord(ch) <= 122::
        output = output + ch

print(output)

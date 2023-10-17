#write a program to reverse the given input string
s="mother"
output=" "
for i in range (len(s)-1,-1):
    output=output+s[i]
print(output)

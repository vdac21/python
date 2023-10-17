#Arrange string charcters such that lowercase letters should come first
str1="VEDAnth"
print(str1)
lower=""
upper=""
for char in str1:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)

stored_str=''.join(lower+upper)
print('Result:',stored_str)
    
    

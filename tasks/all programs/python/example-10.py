ch=input("enter your character: ")

if((ch>='a' and ch<='z')or(ch>='A' and ch<='z')):
    print("the given character", ch,"is an alphabet")
elif(ch>='0' and ch<='9'):
    print("the given character", ch,"is a digit")
else:
    print("the given character", ch,"is a special character")

ch=input("please enter character: ")

if((ch >= 'a' and ch<= 'z')):
    print("the given character", ch, "is an alphabet")
    
elif(ch >= '0' and ch<= '9'):
    print("the given character", ch, "is a digit")
else:
    print("the given chracter", ch, "is a special charcter")

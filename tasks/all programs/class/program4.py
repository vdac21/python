x = input("Enter a string: ")
if len(x) % 2 == 0 and len(x)>=6:
    first = x[0:len(x)//2]
    last = [len(x)//2:len(x)]
    output = firs[len(first)-1] + last[0]
    print(output)
else:
    print("In valid input ")


    

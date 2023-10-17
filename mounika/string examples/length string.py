'''your program should take an even length string as input which length was greater than or equal to 6.
Display the output by combining all the last charcters from the half of the string AND FIRST CHARCTER FROM THE SECOND HALF OF THE STRING
Incase of string is not even length and the number of charcters less than 6, you can display output as "INVALID INPUT STRING" '''

x= input("Enter a string: ")
if len(x)%2==0 and len(x)>=6:
    first=x[0:len(x)//2]
    #last=[len(x)//2 : len(x)=6]
    output=first[len(first)-1]
    print(output)
else:
    print("INVALID INPUT STRING")

from add import *

a=float(input("enter number1: "  ))       
b=float(input("enter number2: "  ))       
option=int(input("enter 1 for addition or enter 2 subtraction"))
if option==1:
    print(add(a,b))
elif option==2:
    print(sub(a,b))
else:
    print("you have choosen wrong option")
                                                   

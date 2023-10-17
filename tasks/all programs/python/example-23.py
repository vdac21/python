num1=int(input("enter a number: "))
num2=int(input("enter a number: "))
operator=str(input("enter the operation you want: "))
if operator=="+":
    print("result is: ", (num1+num2))
elif operator=="-":
    print("result is: ", (num1-num2))
elif operator=="*":
    print("result is: ", (num1*num2))
elif operator=="%":
    print("result is: ", (num1%num2))
elif operator=="/":
    print("result is: ",(num1/num2))

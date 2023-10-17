a=int(input("enter the 1st angle: "))
b=int(input("enter the 2nd angle: "))
c=int(input("enter the 3rd angle: "))
#checking triangle vaild or not
total=a+b+c
if total==180:
    print("this is a valid triangle")
else:
    print("this is an invalid triangle")


x=float(input("enter x-coordinate: "))
y=float(input("enter y-coordinate: "))
s=(x,y)
print(s)
if x>0 and y>0:
    print("it lies in 1st quadrant")
elif x<0 and y>0:
    print("it lies in 2nd quadrant")
elif x<0 and y<0:
    print("it lies in 3rd quadrant")
elif x>0 and y<0:
    print("it lies in 4th quadrant")
else:
    print("it is origin")

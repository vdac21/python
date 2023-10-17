m1=float(input("enter a maths marks"))
m2=float(input("enter a physics marks"))
m3=float(input("enter a chemistry marks"))
tm1=m1+m2+m3
tm2=m1+m2
if m1>=65 and m2>=56 and m3>=50:
 if tm1>=180 or tm2>=140:
     print("it is eligible for professional course")
else:
    print("it is not eligible for professional course")

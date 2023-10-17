sub1=int(input("enter the sub1 marks: "))
sub2=int(input("enter the sub2 marks: "))
sub3=int(input("enter the sub3 marks: "))
total=sub1+sub2+sub3
percentage=total%3
division=total/3
if percentage>=60:
    print("the division is first")
elif 60<percentage>=40:
    print("the division is second")
elif 48<percentage>=36:
    print("the division is pass")
elif percentage<36:
    print("the division is fail")

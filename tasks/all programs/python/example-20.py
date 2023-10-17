sub1=int(input("enter marks of the first subject: "))
sub2=int(input("enter marks of the second subject: "))
sub3=int(input("rnter marks of the third subject: "))
avg=sub1+sub2+sub3/3
if(avg>=90):
    print("grade:E")
elif(avg>=80&avg<90):
    print("grade:V")
elif(avg>=70&avg<80):
    print("grade:G")
elif(avg>=60&avg<70):
    print("grade:A")
else:
    print("grade:F")

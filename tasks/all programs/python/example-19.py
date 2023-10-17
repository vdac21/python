units=int(input("enter number of units you consumed: "))

if(units<=199):
    amount=units*1.20
    print("the total electricity bill:",amuont)
elif(400<units>200):
    amount=unit*1.40
    print("the total electricity bill:",amount)
elif(600<units>=400):
    amount=units*1.80
    print("the total electricity bill:",amount)
elif(units>=600):
    amount=units*2.00
    print("the total electricity bill:",amount)
else:
    amount=units*2.25
    print("the total electricity bill:",amount)
total=amount
print("electricity bill=%.2f"%total)

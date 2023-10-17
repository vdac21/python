temp=int(input("enter a temperature in centigrade: ")
if temp<0:
    print("freezing weather")
elif temp>0 and temp<10:
    print("very cold weather")
elif temp>10 and temp<20:
    print("cold weather")
elif temp>20 and temp<30:
    print("normal in temperature")
elif temp>30 and temp<40:
    print("its hot")
else:
    print("its very hot")

print("list of months: januray, february, march, april, may, june, july, august, september, october, november, december")
monthname=input("the name of the month: ")

if monthname=="february":
    print("no of days:28/29 days")
elif monthname in ("april","june","september","november"):
    print("no.of days:30 days")
else:
    print("no.of days:31 days")

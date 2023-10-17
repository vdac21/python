# Traffic signals

# r  -  stop
# g  -  go
# y  -  strat
# invalid signal

# NOTE : variable names shoudl be meaningful

signal = input("Input Signals: 1-red , 2-green, 3 - yellow : ")

if signal== "1":
    print("Please Stop!")
elif signal == "3":
    print("Please start")
elif signal == "2":
    print("Please Go")
else:
    print("Invalid signal")


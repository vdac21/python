#Accept a list of 5 float numbers as an input from the user



numbers=[]
for i in range(0,5):
    print("enter number at location",i,":")

    item=float(input())
    numbers.append(item)


print(numbers)

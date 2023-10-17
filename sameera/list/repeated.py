v= int(input("enter a value: "))
x=[20,19,25,17,32,17,39,17,20]

print(x)

count=0
if v in x:
    for e in x:
        if e==v:
            count=count+1
    print(f"The elements {v} is repeated {count} time")
else:
    print(f"the element {v} is not found")

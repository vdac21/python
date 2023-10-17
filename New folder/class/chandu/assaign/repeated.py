v = int(input("Enter a value: "))  # 17

x = [20, 19, 25, 17, 32, 17, 39,  17, 20]
print(f"Input: {x}")
count = 0
if v in x:
    for e in x:
        if e == v:
            count = count +1
    print(f"The elemnet {v} is repeated {count} time")
else:
    print(f"The elemnet {v} is not found")

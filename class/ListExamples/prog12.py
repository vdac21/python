x = [10, 30, 78, 18, 92, 17]

max_ele = x[0]
for i in range(1, len(x)):
    if x[i] > max_ele:
        max_ele = x[i]
print(f"Maximum Element from the list : {max_ele}")

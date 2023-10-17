def myreverse(x_list):
    y = []
    for i in range(len(x_list)-1, -1, -1):
        y.append(x_list[i])
    return y
        

x = [10, 20, 30, 40]
#print(f"Input list: {x}")
s = myreverse(x)
print(f"Reversed list: {s}")

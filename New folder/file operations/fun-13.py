
def myreverse(x_list):
    y=[]
    for i in range(len(x)-1, -1, -1):
        y.append(x_list[i])
        return y






x =[10, 20, 30, 40, 50]
print(f"input list: {x}")
s = myreverse(x)
print(f"reversed list: {s}")


# Solution-1
x=[10,5,7,18,78]
z=[]
print(f"Input: {x}")
# Traversing a list indexes from last to first
# by using range function 
for i in range(len(x)-1,-1,-1):
     z.append(x[i])
print(f"Output reverse list different list: {z}")


# Solution-2
x=[10,5,7,18,78]

print(f"Input: {x}")
# Traversing a list indexes till half 
for i in range(0, len(x)//2):
    t = x[i]  # 5
    x[i] =  x[len(x)-1-i]  # x[5-1-1]  # x[3]
    x[len(x)-1-i] = t
print(f"Output reverse list with same list : {x}")


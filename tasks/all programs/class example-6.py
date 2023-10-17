# Replace all elements from the x with square of respective number


x = [2, 4, 6, 8, 12, 16]

"""
print("input",x)
x[0] = x[0] * x[0]
x[1] = x[1] * x[1]
x{2] = x[2] * x[2]
x[3] = x[3] * x{3]
x[4] = x[4] * x[4]
x[5] = x[5] * x[5]
"""

for i in range(0, len(x)):
    #print(i, x[i])
    x[i] = x[i] * x[i]
print(x)

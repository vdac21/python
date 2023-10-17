# Default vs Non-default args


# WAF add two numbers


# add function with two params
def add(x, y):
    c = x+y
    return c


a = 10
b = 20
r = add(a, b) # calling a function 

print(f"1Sum of a={a} and b={b} is r={r}")  # 30


def add(x, y, z):
    c = x+y+z
    return c

a = 10
b = 20
d = 30
r = add(a, b, d) # calling a function 

print(f"2Sum of a={a} and b={b} d={d} is r={r}") # 60


m = 100
n = 200
add(m, n)
print(f"3Sum of m={a} and n={b} is r={r}")  # 300



# Your function shoudl capable to take variable number of
# argumnets 


"""
*args   **kwargs
"""

# sum of all input values

def fun_total(*x):
    s = 0
    for e in x:
        s = s+e
    return s


r = fun_total(a=10)
print(r)

r = fun_total(10,20)
print(r)

r = fun_total(10, 20, 30, 40, 50)
print(r)
r = fun_total(10, 20, 30, 40, 50, 80, 90)
print(r)
r = fun_total(10,50, 80, 90)
print(r)


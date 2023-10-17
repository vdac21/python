def fun_total(*args):
    s=0
    for e in args:
        s=s+e
    return s


r=fun_total(10)
print(r)
r=fun_total(10,20)
print(r)
r=fun_total(10,20,30)
print(r)
r=fun_total(10,20,30,40)
print(r)

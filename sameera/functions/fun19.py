def fun_total(**kwargs):
    s=0
    for k in kwargs:
        s=s+kwargs[k]
    return s
print(fun_total(30))
print(fun_total(a=20,b=20,c=30))
print(fun_total(a=30,b=20,c=30))
print(fun_total(a=40,b=20,c=30))

def fun_total(**kwargs):
    #print(kwargs)
    s = 0
    for k in kwargs:
        s = s+kwargs[k]
    return s





print(fun_total(a=10, b=20, c=30))
print(fun_total(a=10, b=20))
print(fun_total(a=10, b=20, c=30, d=40))

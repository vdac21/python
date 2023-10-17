#WAP print all duplicate elements from the given list


x=[10,20,30,30,40,50,60]
y=[]
z=[]


for e in x:
    if e not in y:
        y.append(e)
    else:
        z.append(e)
print(f"Dups:{z}")
print(f"unique:{y}")
    

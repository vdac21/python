#Wap print all duplicate elements from the given list
#x=[10,25,28,10,78,26,25,35,28]
#output=[10,25,28]

x=[10,25,28,10,78,26,25,35,28]
y=[] #for unique
z=[] #for dups

for e in x:
    if e not in y:
        y.append(e)
    else:
        z.append(e)
print(f"Dups:{z}")
print(f"Unique:{y}")

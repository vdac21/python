#WAP find sum of all the numbers which are divisable by 5


x=[10,20,30,40,50,78]

s=0

for e in x:
    if e%5==0:
        s=s+e
print(s)

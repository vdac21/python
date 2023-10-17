def add(x,y):
    c=x+y
    return c
def sub(x,y):
    c=x-y
    return c
def mul(x,y):
    c=x*y
    return c
def div(x,y):
    try:
        
        c=x/y
        return c
    except:
        print("please give non zero value of second value")
    
    finally:
        print("no error")
v1=int(input("enter a 1st value: "))
v2=int(input("enter a 2nd value: "))


op=input("add-1 sub-2 mul-3 div-4: ")

if op=='1':
    r=add(v1,v2)
    print(r)
elif op=='2':
     r=sub(v1,v2)
     print(r)
elif op=='3':
     r=mul(v1,v2)
     print(r)
elif op=='4':
     r=div(v1,v2)
     print(r)
else:
    print("invaild option")



   




  

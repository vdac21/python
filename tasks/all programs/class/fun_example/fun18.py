# WAP implement basic caluculator application for two numbers

def add(x, y):
    c = x+y
    return c

def sub(x, y):
    c = x-y
    return c

def mul(x, y):
    c = x*y
    return c

def div(x, y):
    c = x//y
    return c

v1 = int(input("Enter a first single : "))
v2 = int(input("Enter 2nd value: "))

op = input("Add-1 Sub-2 Mul-3 Div-4: ")

if op == '1':
    r = add(v1, v2)
    print(f"Output : {r}")
elif op == '2':
    r = sub(v1, v2)
    print(f"Output : {r}")
elif op == '3':
    r = mul(v1, v2)
    print(f"Output : {r}")
elif op == '4':
    r = div(v1, v2)
    print(f"output: {r}")
else:
    print("In valid options")
    
    
    




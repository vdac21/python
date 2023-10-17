# local variable vs global variable


# case1
"""
x = 10 
def fun():
    x = 20
    print(x)

print(x)

# case2

x = 10

def fun():
    x = 20
    print(x)

print(x) #  output : 10 , 20
fun()


x = 10  # global scope 
def fun():
    x = 20
    print(x) # local scope 

print(x)

print(x)    # output : 10, 20, 10
fun()
"""
# case 4
x = 10  # global scope 
def changeGlobaX():
    global x
    x = 20   # hey please chneg variable because suresh requested to change global
    print(x)

print(x)
changeGlobaX()
print(x)    # output : 10, 20, 20


"""
local & global
*args  & **kwargs
default & non default
try & except
"""













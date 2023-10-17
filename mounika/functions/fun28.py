"""
#case1

x=10
def fun():
    x=20
    print(x)
print(x)


#case2

x=10



def fun():
    x=20
    print(x)


print(x)
fun()

#case3

x=10#global scope
def fun():
    x=20
    print(x)#local scope

print(x)
fun()
print(x)
"""
#case4


x=10
def changeGlobaX():
    global x
    x=20
    print(x)
print(x)
changeGlobaX()
print(x)

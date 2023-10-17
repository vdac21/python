#local variable vs global variables

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


x=10
def fun():
    x=20
    print(x)
print(x)
fun()
print(x)


#case4

x=10
def changeGlobax():
    global x
    x=20
    print(x)
print(x)
changeGlobax()
print(x)


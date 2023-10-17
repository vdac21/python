#defining user define module
#In python all.py files will act as module & the file name
#will act as a module name



#Defining user define module
# IN PYTHON ALL .PY Files will act as module & the file name
# will act as a module name

# case1
"""
import calc


r = calc.add(100, 200)
print(r)

"""

# case2
"""
from calc import add

r = add(10, 20)
print(r)


r2 = sub(10, 20) #error
print(r2)
"""
# case3
"""
from calc import add, sub

r = add(10, 20)
print(r)


r2 = sub(10, 20)
print(r2)
"""
# case4
"""
from calc import *


r = add(10, 20)
print(r)


r2 = sub(10, 20) #error
print(r2)

r2 = mul(10, 20) #error
print(r2)
"""
# case5
"""
import calc as c
r = c.add(10, 20)
print(r)
"""
# case6
from calc import add as a
r = a(10, 20)
print(r)

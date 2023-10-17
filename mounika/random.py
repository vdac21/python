"""
import random

list=[1,2,3,4,5,6]
print(random.choice(list))
"""


#Generate random number


import random

def get_otp():
    rnum=random.randrange(10000,99999)
    rnum="GF-"+str(rnum)
    return rnum
print(get_otp())

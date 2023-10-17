# Generate random number

import random


def get_otp():
    rnum=random.randrange(10000,99999)
    rnum="GF-"+str(rnum)
    return rnum
print(get_otp())

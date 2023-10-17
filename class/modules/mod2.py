# Generate randon number 

import random 






def get_otp():
    rnum = random.randrange(1000, 9999)
    rnum= "GF-" + str(rnum)
    return rnum

print(get_otp())
    

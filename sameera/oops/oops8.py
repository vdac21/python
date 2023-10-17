#GUI DEVELOPMENT FRONT END+BACKEND[PYTHON+PYQT5+DB]


"""
common attributes for the customer
cname
cid

"""


class Customer:
    def __init__(self,name,id_):

        #to initilize common attributes of an object
        self.Name=name
        self.id_=id_
    def login(self):

        print(f"Name:{self.Name} and ID:{self.id_}")
c1=Customer('sameera',70)
c2=Customer('mouni',80)
m1=Customer('chandu',90)
c2.login()
c1.login()
m1.login()
#self:the self represent the object reference
#which ever the object your involving the method the self is points to that object




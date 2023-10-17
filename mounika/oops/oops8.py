#GUI DEVELOPMENT FRONTEND+BACKEND[PYTHON+PYQT5+DB]
"""
common attributes for the customer
cname
cid
"""






class customer:
    def __init__(self,name,id_):
#to initilize common attributes of anobject
        self.Name=name
        self.id_=id_
    def login(self):
        print(f"Name:{self.Name} and ID:{self.id_}")
c1=customer("Naresh",400)
c2=customer("suresh",500)
m1=customer("chandu",600)

c2.login()
c1.login()
m1.login()

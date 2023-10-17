#data hiding is based on encapsulation


"""
DEcalre one class , does not give access to another class & hide the data
"""



class bank:
    __balance=10000
    def getbalance(self):
        return self.__balance
class API(bank):
    def printbalance(self):
        return self.__balance

obj=API()
obj.getbalance()
obj.printbalance()



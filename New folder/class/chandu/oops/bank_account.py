class Bankaccount:
    def __init__(self):
        self.__balance=0

    def amount_deposite(self,amount):
        self.__balance+=amount
       # print(self.__balance)

    def amount_withdrawal(self,amount1):
        if(self.__balance>amount1):
            self.__balance-=amount1
        else:
            print("NO sufficient amount ")

    def get_balance(self):
        print(self.__balance)
    
obj_bank=Bankaccount()
obj_bank.amount_deposite(10000)
obj_bank.amount_withdrawal(5000)
obj_bank.get_balance()

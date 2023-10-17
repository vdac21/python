class Bankaccount:
    def __init__(self):
        self.__balance=0

    def amount_deposite(self,amount):
        self.__balance+=amount
       

    def amount_withdrawal(self,amount1):
        if(self.__balance>amount1):
            self.__balance-=amount1
        else:
            print("NO sufficient amount ")

    def get_balance(self):
        print(self.__balance)
    
obj_bank=Bankaccount()
obj_bank.amount_deposite(10000)
obj_bank.amount_withdrawal(15000)
obj_bank.get_balance()


class bank_statement:
    def account_name(self):
     a=input("enter name:")
     print("this account is on",a,"name")
    def withdrawl(self):
     b=int(input("enter the sum you would like to withdraw:"))  
     print(b,"amount is withdrawn")
    def payment(self):
        print("you have already paid")
s1=bank_statement()
s1.account_name()
s1.withdrawl()
s2=bank_statement()
print(s2)
s2.payment()

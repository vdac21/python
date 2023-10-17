class Employee:    
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def get_employee_info(self):
        print ("name {}, age {}, salary{}". format(self.name,self.age,self.salary))
    def set_salary (self,amount):
        self.salary=amount
    def get_salary(self):
        return self.salary
e1=Employee("satya", 45,10)
e2=Employee("chandu", 46,11)
e1.get_employee_info()
e2.get_employee_info()
e1.set_salary(20)
print (e1.get_salary())

class Employees(): 
 
   def Name(self): 
       print ("Employee Name: Khush")
 
class salary(Employees):
   def Salary(self):
       print ("Salary: 10000")
 
class Designation(salary,Employees):
   def desig(self):
       print ("Designation: Test Engineer")
 
call = Designation()
call.Name()
call.Salary()
call.desig()
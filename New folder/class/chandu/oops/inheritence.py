#multilevel inheritence
class employees():  #grandfather
    def name(self):
        print("employee name:kushi")
class salary(employees):  #father
    def Salary(self):
        print("Salary:100000")
class Designation(salary):    #son
    def desig(self):
        print("Designation:Test Engineer")

call=Designation()  #object creation
call.name()
call.Salary()
call.desig()
        
#multiple inheritence

class employees():  #father
    def name(self):
        print("employee name:kushi")
class salary():  #mother
    def Salary(self):
        print("Salary:100000")
class Designation(salary,employees):    #son
    def desig(self):
        print("Designation:Test Engineer")

call=Designation()  #object creation
call.name()
call.Salary()
call.desig()



#Hierarchical inheritence


class Brands:
    brand_name_1 = "Amazon"
    brand_name_2 = "ebay"
    brand_name_3 = "olx"
class products(Brands):
    prod_1="Online Ecommerce store"
    prod_2="Online store"
    prod_3="Online Buy Sell store"
class popularity(Brands):
    prod_1_popularity=100
    prod_2_popularity=80
    prod_3_popularity=60
class value(Brands):
    prod_1_value="Excellent value"
    prod_2_value="Better value"
    prod_3_value="Good value"

obj_1=products()
obj_2=popularity()
obj_3=value()
print(obj_1.brand_name_1+"is an "+obj_1.prod_1,obj_2.brand_name_1+"is "  +obj_3.prod_1_value)

    
    
    
    
    


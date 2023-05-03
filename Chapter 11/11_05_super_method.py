class Person:
    country = "India"
    
    def __init__(self):
        print("Initialization person..") 
        
    def takeBreath(self):
        print("I am breathing.......")
        
class Employee:
    company = "Honda"
    
    def __init__(self):
        super().__init__()
        print("Initialization Emoloyee..")
    
    def getSalary(self):
        print("Salary is {self.salary}")
        
    def takeBreath(self):
        # super().takeBreath()
        print("I am an Employee so i am lickily breathing....")
        
class Programmer(Employee):
    company = "Fiverr"
    
    def __init__(self):
        super().__init__()
        print("Initialization Programmer..")
        
    def  getSalary(self):
        print("No salary to programmer")
        
    def takeBreath(self):
        super().takeBreath()    # It will help to print it's parent calss's takeBreath method also.. 
        print("I am an Programmer so i am lickily breathing+++....")
       
        
p = Person()  
p.takeBreath()

e = Employee()
e.takeBreath()

pr = Programmer()
pr.takeBreath() 

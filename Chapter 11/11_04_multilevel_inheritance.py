class Person:
    country = "India"
    
    def takeBreath(self):
        print("I am breathing.......")
        
class Employee:
    company = "Honda"
    
    def getSalary(self):
        print("Salary is {self.salary}")
        
    def takeBreath(self):
        print("I am an Employee so i am lickily breathing....")
        
class Programmer(Employee):
    company = "Fiverr"
    
    def  getSalary(self):
        print("No salary to programmer")
        
p = Person()
p.takeBreath()
e = Employee()
e.takeBreath()
pr = Programmer()
pr.takeBreath()     # It will use the latest function..(nearest parent class)
print(pr.country)
print(pr.company)
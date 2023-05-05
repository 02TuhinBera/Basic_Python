class Employee:     # It is Base Class
    company = "Google"     
    
    def showDetails(self):
        print("This is an employee")
    
class Programmer(Employee):    # It is Child Class
    language = "Python"
    company = "Youtube"
    def getLanguage(self):
        print(f"The language is {self.language}")
        
    def showDetails(self):
        print("This is a programmer")
        
      
e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()    # First it will check if the fuction is present in child class, if yes then it will print as well.
p.getLanguage()    # if not, then it will check if the fuction is present in the base class and print as well.
print(p.company) 
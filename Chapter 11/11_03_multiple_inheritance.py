class Employee:
    company = "visa"
    eCode = 110
    
class Freelancer:
    company = "Fiverr"
    level = 0
    
    def upgradeLevel(self):
        self.level = self.level + 1
        
        
class Programmer(Employee, Freelancer):
    name = "Rohit"

p = Programmer()
p.upgradeLevel()
print(p.level)
print(p.company) # It will print "Visa" Because in the child class, we first defined or inheritance Employee and nxt Freelancer.



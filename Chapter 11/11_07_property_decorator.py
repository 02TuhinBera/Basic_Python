class Employee:
    company = "Instagram"
    salary = 6500
    salarybonus = 500
    # totalSalary = 6100
    
    @property
    def totalSalary(self):
        return self.salary + self.salarybonus 
    
e = Employee()
print(e.totalSalary)
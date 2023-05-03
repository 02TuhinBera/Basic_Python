class Employee:
    company = "Camel"
    salary = 100    # Class attribute
    location = "Delhi"
    
    # def changeSalary(self, sal):
    #     # self.salary = sal            # Instance attribute
    #     self.__class__.salary = sal    # It will help to change the class attribute

    @classmethod                          # This method is also help us to change the class attribute.
    def changeSalary(cls, sal):
        cls.salary = sal
        
        
e = Employee()
print(e.salary)
e.changeSalary(500)
print(e.salary)
print(Employee.salary)
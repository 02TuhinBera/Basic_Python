class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")
        
    @staticmethod
    def greet():
        print("Good Morning, Sir")
        
    @staticmethod
    def time():
        print("The time is 10 am in the morning")
    
        
tuhin = Employee()
tuhin.salary = 1000
tuhin.greet()  # Employee.greet()   # use of static method without ysing self parameter
tuhin.time()
    
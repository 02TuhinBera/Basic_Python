class Employee:
    company = "Google"
    
    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created")
    
    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")
        
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")
        
    @staticmethod
    def greet():
        print("Good Morning, Sir")
        
    @staticmethod
    def time():
        print("The time is 10 am in the morning")
    
tuhin = Employee("Tuhin", 1000, "Youtube")
# tuhin = Employee()     --> this will throw a error  (missing three required positional)
tuhin.getDetails()
class Employee:
    company = "Google"
    def getSalary(self, signature):
        # print("Salary is 100k")
        print(f"Salary for this employee working in {self.company} is {self.salary}\n {signature}")
    
tuhin = Employee()
tuhin.salary = 1000
tuhin.getSalary("Thanks")       # this line and the line under this works as same
# Employee.getsalary(tuhin)

    
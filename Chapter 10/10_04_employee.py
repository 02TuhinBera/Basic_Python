class Employee:
    company = "Google"
    salary = 500 
     
tuhin = Employee()
harry = Employee()
tuhin.salary = 3000

# harry.salary = 4000  # here we are just checking....

print(tuhin.company)
print(harry.company)
Employee.company = "Youtube"
print(tuhin.company)
print(harry.company)

# creating instance attrubute salary for both the objects.
print(tuhin.salary)
print(harry.salary)
 
''' If there is a class attrubutr and also a objects attribute
first it will check that --> Is attribute in the object? 
next it will check that --> Is attribute in the class?'''

# Below line throw an error as address is not present in the instance/class
print(tuhin.address)
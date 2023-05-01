class Calculator:
    def __init__(self, num):
        self.number = num
    
    def square(self):
        print(f"The value of the {self.number} square is {self.number**2}")
    
    def squareRoot(self):
        print(f"The value of the {self.number} square root is {self.number**0.5}")
    
    def cube(self):
        print(f"The value of the {self.number} cube is {self.number**3}")
    
    @staticmethod
    def greet():
        print("*****Hello, i welcome to the best calculator of the world*****")
a = Calculator(3)
a.greet()
a.square()
a.squareRoot()
a.cube()
        
        
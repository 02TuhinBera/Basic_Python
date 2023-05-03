class Animals:
    animalType = "Mamals"
    
class Pets:
    color = "White"
    
class Dog:
    @staticmethod
    def bark():
        print("Bow bow!")
        
d = Dog()
d.bark()
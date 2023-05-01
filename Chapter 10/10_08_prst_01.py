class programmer:
    company = "Micresoft"
    
    def __init__(self, name, product):
        self.name = name
        self.product = product
    
    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} andd product is {self.product}")
    
tuhin = programmer("Tuhin", "Skype")
luffy = programmer("Luffy", "Github")
tuhin.getInfo()
luffy.getInfo()
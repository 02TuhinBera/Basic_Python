class RailwayForm:  # her we declaring the class....
    fornType = "RailwayForm"
    def printData(self):
        print(f"Name is: {self.name}")
        print(f"Train is: {self.train}")
    
tuhinApplication = RailwayForm()  # here we are declaring the object...
tuhinApplication.name = "Tuhin"
tuhinApplication.train = "Rajdhani Express"
tuhinApplication.printData()

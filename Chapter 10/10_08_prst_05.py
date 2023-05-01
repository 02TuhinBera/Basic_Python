class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the trai are {self.seats}")

    def fareInfo(self):
        print(f"The price of the ticket is: rs {self.fare}")

    def bookTicket(self):
        if (self.seats > 0):
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry! This train is full! Kindly try in tatkal")


intercity = Train("Intercity Express: 450025", 90, 300)
intercity.getStatus()
intercity.fareInfo()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()

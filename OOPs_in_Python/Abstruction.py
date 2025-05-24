# Abstruction and Encapsulation
# Abstruction is used to hiding the details from users and showing the essential data to user.
# Encapsulation: Wrapping a data and function into a single units(objects)

class Car():
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.acc = True
        self.clutch = True
        print("Car started ...")

car1 = Car()
car1.start()

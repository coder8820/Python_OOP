class Car:
    def __init__(self, start, stop, color, model, year):
        self.start = start
        self.stop = stop
        self.color = color 
        self.model = model
        self.year = year
    
    def start_engine(self):
        print(f"The {self.color} {self.model} engine has started.")
    
    def stop_engine(self):
        print(f"The {self.color} {self.model} engine has stopped.")

    def display_info(self):
        print(f"Car Start: {self.start}")
        print(f"Car Stop: {self.stop}")
        print(f"Car Color: {self.color}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")
class ToyotaCar(Car):
    def __init__(self, start, stop, color, model, year, fuel_type, mileage):
        super().__init__(start, stop, color, model, year)
        self.fuel_type = fuel_type
        self.__mileage = mileage # private variable
    def display_info(self):
        super().display_info()
        print(f"Fuel Type: {self.fuel_type}")
        print(f"Mileage: {self.mileage}")
    

# Creating an instance of the ToyotaCar class
c1 = ToyotaCar("Start", "Stop", "Red", "Toyota Corolla", 2025, "Petrol", 15)

c1.display_info()
print("\n-------------------------------------\n")
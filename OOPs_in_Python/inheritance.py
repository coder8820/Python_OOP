class Baltistan:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def display_info(self):
        print(f"Name: {self.name}, Area: {self.area} sq km")
class Skardu(Baltistan):
    def __init__(self, name, area, population):
        super().__init__(name, area)
        self.population = population

    def display_info(self):
        super().display_info()
        print(f"Population: {self.population}")
class SkarduCity(Skardu):
    def __init__(self, name, area, population, altitude):
        super().__init__(name, area, population)
        self.altitude = altitude
    def display_info(self):
        super().display_info()
        print(f"Altitude: {self.altitude} meters")

# Creating an instance of the Skardu class
Sk = SkarduCity("Baltistan", 8000, 60000, 2500)
# Displaying information about the Skardu instance
Sk.display_info()
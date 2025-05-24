#Q1- Define a circle class to create a circle with radius r using the constructor

class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def Area(self):
        area = (22/7) * self.radius ** 2
        return area
    
    def Perimeter(self):
        peri = 2 * (22/7) * self.radius    
        return peri
    
c1 = Circle(21)

print(c1.Area())
print(c1.Perimeter())
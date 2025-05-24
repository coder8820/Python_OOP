# we use @property decorator at any method in the class to use the method as a property

class Student:
    def __init__(self, compu, math, phy):
        self.compu  = compu
        self.math = math
        self.phy = phy
    
    # def calcuPercentage(self):
    #     self.percentage = str((self.sum) / 3) + "%"
    
    @property
    def percentag(self):
        return str((self.compu + self.math + self.phy) / 3) + "%"

s1 = Student(88, 98, 78)
print(s1.percentag)
s1.phy = 50
s1.compu = 90
print(s1.percentag)

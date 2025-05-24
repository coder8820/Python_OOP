class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real,"i +", self.img,"j")
    
    def __add__(self,num2):   # we defined a dunder function
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self,num2):
        subReal = self.real - num2.real
        subImg = self.img - num2.img
        return Complex(subReal, subImg)



n1 = Complex(2,7)
n1.showNumber()

n2 = Complex(5,2)
n2.showNumber()
print('----------')

# num3 = n1.add(n2)
num3 = n1 + n2
num3.showNumber()
print('---Subtraction------')
num3 = n1 - n2
num3.showNumber()
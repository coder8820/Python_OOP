class Person:
    __name = "John Doe"  # Private attribute
    __age = 30  # Private attribute

    def __helo(self):
        print("Hello, this is a private method!", self.__name)
    
    def wecome(self):
        print("Welcome to the private method demonstration!")
        self.__helo()

p1 = Person()
p1.wecome()
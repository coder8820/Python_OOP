# del keyword: used to delete object properties or object itself
# del s1.name  or del s1 

# class Student:
#     def __init__(self, name):
#         self.name = name

    
# s1 = Student("kumail")
# del s1.name
# print(s1.name)


# =====> Private(like) attributes and methods <=======

# Conceptual Implementation in python:
#  Private attribute and methods are meant to be used only with in the class and are not accessible from outside of the class

class Account:
    def __init__(self, name, passw, section):
        self.__name = name
        self.__passw = passw
        self.section = section
    
    def reset_pass(self):
        print(self.__passw)
        print(self.__name)
    
    def studets(self):
        print("Student name is: ", self.__name)
        print("Student paswe : ", self.__passw)
        print("Student paswe : ", self.section)
    
    @staticmethod
    def display():
        print('Everything Displayed')
        print('This is Displying static method')



s1 = Account('admin', 'admin','A')
s2 = Account('kumail', '1234','B')

# print(s1.name) # this will give error because __name is private
print(s1.reset_pass())
s1.display()
s1.studets()
s2.studets()

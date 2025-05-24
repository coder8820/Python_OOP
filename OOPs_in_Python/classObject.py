class student:

    # default constructor
    def __init__(self):
        pass

    # parameterized constructor
    def __init__(self,name, rollno):
        self.name = name,
        self.rollno = rollno
        print("Constructor called")
    
    def display(self):
        print("Name: ", self.name)
        print("Roll No: ", self.rollno)

name = input("Enter your name: ")
rollno = str(input("Enter your roll number: "))

s1 = student(name,rollno)
# s1.display()
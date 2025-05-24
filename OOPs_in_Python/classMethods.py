class student:

    def __init__(self,name, age):
        self.name = name
        self.age = age
        self.university = "Baltistan University"
        self.department = "Computer Science"
    
    def display(self):
        print("You are welcome mister ",self.name)
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("University: ", s1.university)
        print("Department: ", s1.department)
        
    def get_marks(self,marks):
        self.marks = marks
        print("Marks: ", self.marks)


s1 = student("hacker", 23)
s1.display()
s1.get_marks(89.9)
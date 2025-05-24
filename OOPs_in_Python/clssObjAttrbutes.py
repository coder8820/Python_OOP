class student:
    university = "Baltistan University"  # class attribute
    department = "Computer Science"  # class attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("University: ", student.university)
        print("Department: ", s1.department)

s1 = student("hacker", 23)
s1.display()

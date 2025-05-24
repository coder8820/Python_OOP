# Q1. create a student class with name, marks of 3 subjects as arguments in constructor
#      then create a method to calculate and print the average of marks

# class Student:
#     def __init__(self, name, marks1, marks2,marks3):
#         self.name = name
#         self.marks1 = marks1
#         self.marks2 = marks2
#         self.marks3 = marks3
    
#     def calculate_average(self):
#         total_makrs = self.marks1 + self.marks2 + self.marks3
#         average = total_makrs / 3
#         print(f"Average marks of {self.name} is: {average:.2f}")

# s1 = Student("Kumail", 85, 90, 79)
# s1.calculate_average()

class Student:
    def __init__(self, name,marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def get_university():
        print( "Baltistan of University")
    
    @staticmethod
    def Link_department():
        print("Computer Science")
        print("Biology")
        print("English Department")
    
    def average(self):
        total_marks = sum(self.marks)
        average = total_marks / len(self.marks)
        print(f"Average marks of {self.name} is: {average:.2f}")

s1 = Student("Kumail", [87,90,88])
s1.get_university()
s1.Link_department()
s1.average()
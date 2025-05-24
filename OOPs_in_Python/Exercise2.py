#Q2- Define an Employee class with attribute role,depart,salary. This class should have showDetail method.
#    Create an Engineer class that inherits properties from Employee

class Employee:
    def __init__(self, rol, department, salary):
        self.rol = rol
        self.department = department
        self.salary = salary
    
    def showDetails(self):
        print("rol: ",self.rol)
        print("Department: ",self.department)
        print("Salary: ",self.salary)

class Engineer(Employee):
    def __init__(self,name,age,rol,department,salary):
        self.name = name
        self.age = age
        super().__init__(rol,department,salary)
    def showDetails(self):
        print('name: ',self.name)
        print('age: ', self.age)
        super().showDetails()

e1 = Engineer('kumail',23,'Developer','BSCS', 980099)
e1.showDetails()

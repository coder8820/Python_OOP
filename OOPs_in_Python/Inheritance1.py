class Department:
    def __init__(self, name, location, head, num_of_employees, num_of_projects, budget):
        self.name = name
        self.location = location
        self.head = head
        self.num_of_employees = num_of_employees
        self.num_of_projects = num_of_projects
        self.budget = budget
    def display_info(self):
        print(f"Department Name: {self.name}")
        print(f"Location: {self.location}")
        print(f"Head: {self.head}")
        print(f"Number of Employees: {self.num_of_employees}")
        print(f"Number of Projects: {self.num_of_projects}")
        print(f"Budget: {self.budget}")
class ITDepartment(Department):
    def __init__(self, name, location, head, num_of_employees, num_of_projects, budget, projects, programming_lang, tools):
        super().__init__(name, location, head, num_of_employees, num_of_projects, budget)
        self.projects = projects
        self.programming_lang = programming_lang
        self.tools = tools
    def display_info(self):
        super().display_info()
        print(f"Projects: {self.projects}")
        print(f"Programming Languages: {self.programming_lang}")
        print(f"Tools: {self.tools}")


c1 = ITDepartment("IT Department", "University of Baltistan", "Javeed Sab", 150, 15, 9000000, ["Web Application", "Android Application"], ["Python", "Java",'C#'], ["Git", "Docker", "Jenkins"])
c2 = ITDepartment("IT Department", "University nvidea", "mark Zagerbur", 850, 515, 999880000, ["SpaceX", "Netfilx"], ["Python", "Java",'C#'], ["Git", "Docker", "Jenkins"])
c1.display_info()
print("\n-------------------------------------\n")
c2.display_info()
# Creating an instance of the ITDepartment class
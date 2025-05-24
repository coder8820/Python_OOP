class Person:
    name = 'anonymous'

    # def changeName(self, name,age,gender):
    #     Person.name = name
    #     self.__class__.gender = gender
    #     Person.age = age

    @classmethod
    def changeName(cls, name, age, gender):
        cls.name = name
        cls.age = age
        cls.gender = gender
        


p1 = Person()
p1.changeName('ali ahmed',23,'male')
print(p1.age)
print(Person.age)
print(Person.name)
print(Person.gender)
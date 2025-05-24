class A:
    def __init__(self,age):
        self.name = "A"
        self.age = age

    def greet(self):
        return f"\n first Hello from {self.name}, age {self.age}"
class B:
    def __init__(self):
        self.name = "B"

    def greet(self):
        return f"\n thrd last Hello from {self.name}"
class C(A, B):
    def __init__(self,age):
        A.__init__(self,age)
        B.__init__(self)
        self.name = "C"

    def greet(self):
        return f"\n secnd last Hello from {self.name}, {A.greet(self)}, {B.greet(self)}"

class D(C):
    def __init__(self, age):
        C.__init__(self, age)
        self.name = "D"
    def greet(self):
        return f"\n last Hello from {self.name}, {C.greet(self)}"

# Creating an instance of class C
d1 = D(23)
# Calling the greet method
print(d1.greet())
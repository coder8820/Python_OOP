import random   # Random is a module, 

print(random.randrange(1,10))
print("----------------------")
a = 5
b = "Helo World"
c = 3.3
d = True
fruits = "Orange","Abble","Banana"
x,y,z  = fruits
print("--------------------")
print(x)
print(y)
print(z)
print("--------------------")
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print("-------------------")

x = "awesome"

def myfun():
    global x
    x = "fantastic"
    print("Python is "+ x)

myfun()
print("python is "+ x)

k = """ This is mister Kumail From University of Baltistan Sakrdu, BSCS student 5th semester"""

print(len(k),"Characters")
if "Kumail" in k:
    print("Yes, kumail is present")
if "jameel" not in k:
    print("not exist")
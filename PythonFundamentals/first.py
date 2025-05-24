# # This is a comment
# name = 'Kumail Abbas'
# age = 23.5
# year = 2023
# name1 = None
# old = False
# young = True
# # print('I am', name, 'my age is', age)

# def add(a, b):
#     return a + b
# print(type(name))
# print(type(age))
# print(type(year))
# print(type(name1))
# print(type(old))
# print(type(young))
# print("Addition of a and b = ",(add(2,3)))



# ---------------

# a = 10
# b = 20
# A = a + b
# B = a - b
# print("Addition of a and b = ", A)
# print("Subtraction of a and b = ", B)
# print("Multiplication of a and b = ", a * b)


# ------------------- exericse 
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# addition = num1 + num2
# subtraction = num1 - num2
# multiplication = num1 * num2
# division = num1 / num2

# if num2 != 0:
#     division = num1 / num2
# else:
#     division = "undefined (division by zero)"

# print("Addition: {num1} + {num2}  = ", addition)
# print("Subtraction: {num1} - {num2}  = ", subtraction)
# print("Multiplication: {num1} * {num2}  = ", multiplication)
# print("Division: {num1} / {num2}  = ", division)



# ------------- Calculator ---------------

a = 1
b = 11


for i in range(a, b):  # Tables from 1 to 10
    print(f"Multiplication Table for {i}")
    print("-" * 26)
    for j in range(a, b):  # Each table from 1 to 10
        print(f"\t{i} x {j} = {i * j}")
    print("_"* 26)
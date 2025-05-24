# Functions:-----> is a block of code that performs a specific task. It is a reusable piece of code that can be called
#  multiple times in a program. Functions help to break down a
#  program into smaller, manageable parts, making it easier to read and maintain.


# def message():
#     print("Hello, this is a function")
# # message()

# for i in range(5):
#     message()
#     i += 1



# def sumCal(x,y):
#     sum = x + y
#     return sum

# sum = sumCal(10,20)
# print("The sum of 10 and 20 is: ", sum)


#  find average of 3 numbers

# def average(x,y,z):
#     sum = x+y+z
#     avg = sum / 3
#     return avg

# output = average(10,80,40)
# print("The average of 10, 20 and 30 is: ", output)

# print("KumailShabbir", end=" ")
# print("University of Baltistan")


#  -------------- Exercise Questions ----------------
# 1.wap find the length of a list using function

# cities = ["Karachi", "Lahore", "Islamabad", "Peshawar", "Quetta"]
# indiaCities = ["Delhi", "Mumbai", "Bangalore", "Hyderabad", "Chennai"]

# def print_len(list,list2):
#     lenth = len(list) + len(list2)
#     print("the length of the list is ",lenth)

# print_len(cities, indiaCities)


# Question 2: wap print the element of the list in a single line using function

# heroes = ["Superman", "Batman", "Spiderman", "Ironman", "Thor"]
# vilans = ["Joker", "Green Goblin", "Loki", "Thanos", "Venom"]
# def print_list(list,list2):
#     for i in list:
#         print(i, end=" ")
#     print("\n")
#     for i in list2:
#         print(i, end=" ")

# print_list(heroes, vilans)


# Question 3: wap find the factorial of a number using function n is the parameter

# num = int(input("Enter a number: "))

# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i   
#     return fact
# output = factorial(num)
# print(f"The factorial of {num} is: ", output)


# Question 4: wap convert usd to pkr using function
# 1 usd = 280 pkr
# 1 euro = 300 pkr
# 1 pound = 350 pkr

# usd = float(input("Enter the amount in USD: "))
# euro = float(input("Enter the amount in Euro: "))

# def usd_to_pkr(usd, euro):
#     pkr = usd *280
#     pkr1 = euro * 300
#     return pkr, pkr1
# output = usd_to_pkr(usd,euro)
# print(f"The amount in PKR & EURO is: {output}")


# Question 5:

numb = int(input("Enter any Number: "))

def showResult(val):
    if val % 2 == 0:
        print(f"{val} is even Number")
    else:
        print(f"{val} is odd Number")

showResult(numb)
# Definition of a for loop
# Used for secquential traversal. For traversing list, strings, tuples, dictionaries, sets,arrays,etc.
# The for loop can also be used to iterate over a string
#

# fruits = ['apple', 'banana', 'cherry']
# num = [10, 2, 3, 4, 5]
# vegitables = ['carrot', 'potato', 'onion', 'ladyfinger', 'cucumber', 'tomato', 'brinjal']
# for items in fruits:
#     print(items)

# for val in num:
#     print("The number is: ", val)

# for vegi in vegitables:
#     if(vegi == 'tomato'):
#         print("Found the tomato", vegi)
#         break 
#     # when use break, it will break the loop and else statement did not execute
#     print("The vegetable is: ", vegi)
# else:
#     print("Printed vegetable list")

# Question: 1

# arr = [1,2,3,4,5,6,7,8,9]
# # x = 8
# idx = 0
# for i in arr:
#     print("this is the required ",i*i)
#     if i == 8:
#         print("Found the number ",idx)
#         continue
#     idx += 1
#     i += 1

# Question: 2
# Range function returns a sequence of numbers, starting from 0 by default, and increments by 1, stops at a specified number
# arr = [1,2,3,4,5,6,7,8,9]
# for i in range(arr[0], arr[-1]+1):
#     print(i)

# for i in range (5):
#     print(i+1)

# for i in range(start, stop, step): conditions
# for i in range (0, 40, 5):
#     print(i)

# Question 1
# Print numbers from 1 to 100
# for i in range(1, 101):
#     print(i)


# Print number 100 to 1
# for i in range(100, 0, -1):
#     print(i)

# Print a multiplication table of a number x
# x = int(input("Enter a number:"))
# for i in range(1,11):
#     print(f"{x} * {i} = {x*i}")

# ------------- Pass statement ---------------

# The pass statement is a null operation; nothing happens when it executes. It is syntactically required to have a statement in a block.
# It is used when a statement is required syntactically but you do not want any command or code to execute.
# It is a placeholder for future code. It is used when you are working on a new function, class, or loop and you want to implement it later.

# Example of pass statement
# for i in range(5):
#     pass

# print("some work will do later")




# -------------------- Exercise Questions ----------------
# 1. wap to find the sum of first 10 number using for loop
# arr = [1,2,3,4,5,6,7,8,9]
# sum = 0
# for i in arr:
#     sum += i
# print("The sum of first 10 numbers is: ", sum)

# 2. wap to find the factorial of a number using while loop

n = int(input("Enter a number: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(f"The factorial of {n} is: ", fact)

# x = int(input("Enter a number: "))
# fact = 1
# for i in range(1, x+1):
#     fact *= i
# print(f"The factorial of {x} is: ", fact)
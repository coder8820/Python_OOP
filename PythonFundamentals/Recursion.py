#  ----------------- Recursion -----------------
# Definition: When a function calls itself repeatedly until a base case is met.

# def show(n):
#     if n == 0:
#         return
#     else:
#         print(n)
#         show(n-1)

# show(5)

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))


# Exercise 1: wite the sum of n natural numbers using recursion

# def doSome(n):
#     if n == 0:
#         return 0
#     return doSome(n-1) + n

# print(doSome(5))


# Exercise 2: print the list using recursion

def printList(list,index=0):
    if index == len(list):
        return
    print(list[index])
    printList(list,index+1)

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
printList(fruits)
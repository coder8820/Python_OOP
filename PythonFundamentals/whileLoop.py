# ------- While Loops -----------

# count = 1
# while count<=5:
#     print(' Hello World',count)
#     count += 1

# print("\nEnd of while loop")

# i = 5
# while i >= 1:
#     print('printing reversly ',i)
#     i -= 1

# Print the element of the following list using loop
# num = 1
# while num<=10:
#     print(num*num)
#     num += 1

# print the Multiplication Table of any number 1 to 10
# num = 1
# while num<=10:
#     print('5 *',num, '=',5*num)
#     num += 1

# -----------------------
# question  Search Element in the tuple

# nums = (13,2,6,8,45,34,23,12,34,23,12,56,78,90)

# x = 56
# y = 12

# i = 0
# while i <= len(nums):
#     print("Number at index", i, "is", nums[i])
#     if nums[i] == x:
#         print("Found", x, "at index", i)
        
#     if(i==10):
#         print('break statement',i)
#         break
#     i += 1

# -------------- Break and Continue--------------


# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# i = 0

# while i < len(arr):
#     if(i == 5):
#         i+=1
#         continue
#     print(arr[i])
#     i += 1

# while i < len(arr):
#     if(i == 6):
#         i += 1
#         continue
#     print(arr[i])
#     i += 1

# ----------- print Even numbers only ------------

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# i = 0
# while i < len(arr):
#     if arr[i] % 2 == 0:
#         print(arr[i])
#         i += 1
#     else:
#         i += 1
#         continue
#     i += 1

# ----------- print Odd numbers only ------------

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(arr):
    if arr[i] % 2 != 0:
        print(arr[i])
        i += 1
    i += 1
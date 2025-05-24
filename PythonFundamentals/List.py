# List in Python
# A built-in data type in Python that is used to store a collection of items, different data type.
# Lists are mutable, meaning you can change their content without changing their identity.

marks = [90, 80, 70, 60, 50]
print(marks)
sort = marks.sort(reverse=True)  # Sorting the list in ascending order
print(sort)  # Printing the sorted list
print(marks)  # Printing the sorted list
print(type(marks))
print(marks[0])  # Accessing the first element of the list
print(marks[1])  # Accessing the second element of the list
print(marks[2])  # Accessing the third element of the list
print(marks[3])  # Accessing the fourth element of the list
print(marks[4])  # Accessing the fifth element of the list
print(marks[-1])  # Accessing the last element of the list

print("------------- List Slicing --------------")
print(marks[0:3])  # Accessing the first three elements of the list
print(marks[1:4])  # Accessing the second to fourth elements of the list
print(marks[2:])  # Accessing all elements from the third element to the end of the list

print("------------- List Methods --------------")
print(marks)  # Printing the original list
marks.append(100)  # Adding an element to the end of the list
print(marks)  # Printing the list after appending an element
marks.insert(2, 95)  # Inserting an element at index 2
print(marks)  # Printing the list after inserting an element
marks.remove(80)  # Removing the first occurrence of the element 80 from the list
print(marks)  # Printing the list after removing an element
marks.remove(100)
print("100 is removed from the list",marks)

print("------------- List --------------")

student = ['kumail',23,True,45.5]
print(student)  # Printing the list with different data types
print(student[0])
student[0] = 'AroojFatima'
print(student)

list = [1,5,3,7,3,2,7,8,9,0,4,6]
# list.reverse()
list.sort(reverse=True)  # Sorting the list in descending order
print(list)  # Reversing the list

fruits = ['banana', 'apple', 'mango', 'orange']
fruits.insert(2, 'kiwi')  # Inserting 'kiwi' at index 2
print(fruits)  # Printing the list after inserting 'kiwi'
fruits.remove('apple')  # Removing 'apple' from the list
print(fruits)  # Printing the list after removing 'apple'
fruits.append('grape')  # Appending 'grape' to the end of the list
print(fruits)  # Printing the list after appending 'grape'
fruits.pop(1)
print(fruits)  # Removing the element at index 1
fruits.pop()  # Removing the last element from the list
print(fruits)  # Printing the list after removing the last element
fruits.clear()  # Clearing the entire list
print(fruits)  # Printing the empty list
#  Python can be used to perform the Operations on a file.(Read, Write data).
# Types of all files
# 1. Text files: (.txt,.doxs,.log,etc)
# 2. Binary files: (.mp4, .mov, .png, .jpeg etc)


#-----------> Create a file -------------
# f = open("demo1.txt", "w")
# f.close()


# ----------> Write in a file ------------

# f = open("demo1.txt", 'a')
# data = f.write("This is my demo1 file created for strong practices")
# f.close()

# ---------> Read a file --------------
# f = open("demo1.txt", 'r')
# data = f.read()
# print(data)
# f.close()


# ----------> Again Practice --------------

# create_file = open("demo2.txt", 'w')
# create_file.close()

#  -----------> Write in a file --------------

# read_file = open("demo2.txt", 'a')
# data = read_file.write("This is my demo2 file created for strong practices")
# read_file.close()

# ----------> Read a file --------------

# read_file = open("demo2.txt", 'r')
# data = read_file.read()
# print(data)
# read_file.close()





# f = open("demo.txt", "rt")
# # data = f.read(13)
# data = f.readline()
# line2 = f.readline()
# # print(data)
# print(data)
# print(line2)
# print(type(data))
# f.close()


# f = open("demo.txt",'a')

# data = f.write("\tThen i will learn React js from Sharada also")
# print(data)

# f.close()

# f = open("sample.txt","r")
# data = f.read()
# print(data)
# f.close()

# File input/Output system in python is very important.
# It is used to read and write data from and to files.
# When we use the open() function, we need to specify the mode in which we want to open the file.
# The modes are:
# 1. 'r' - Read mode: This is the default mode. It opens the file for reading.
# 2. 'w' - Write mode: This mode opens the file for writing. If the file already exists, it will be overwritten.
# 3. 'a' - Append mode: This mode opens the file for appending. If the file does not exist, it will be created.
# 4. 'x' - Exclusive creation mode: This mode opens the file for writing, but only if it does not already exist.
# 5. 'b' - Binary mode: This mode opens the file in binary format. It is used for non-text files.
# 6. 't' - Text mode: This mode opens the file in text format. It is used for text files.


# ----------------> File Handling in Python ----------------
# File handling is the process of creating, reading, writing, and deleting files in Python.

# with open("demo1.txt", "r") as f:
#     data = f.read()
#     print(data)

# f = open("demo1.txt", 'r')
# data = f.read()
# print(data)
# f.close()



# 1. Creating a file
# create_file = open("demo1.txt", 'w')
# create_file.close()

# with open("demo1.txt", 'a') as f:
#     data = f.write("This is my demo1 file created for strong practices")
#     f.close()

with open("demo.txt", 'r') as f:
    data = f.read()
    print(data)
    f.close()
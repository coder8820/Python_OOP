# --------  Write in a file  by using these instructions

# with open("docum.txt", 'a') as f:
#     data = f.write("This is the last file i created for Practice of the python File handling system")
#     print(data)
#     f.close()


# with open("demo2.txt", 'a') as f:
#     data = f.write("The file demo1.txt created by these Python Instructions")
#     print(data)
#     f.close()

with open("demo2.txt", 'r') as f:
    data = f.read()
    print(data)
    f.close()
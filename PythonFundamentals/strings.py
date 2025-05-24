str1 = "this is strings.We are creating it in python"
str2 = " this is Concatination we used in python"
concate = str1+str2
print(concate)
# print(len(concate),"\tthis the length of the strings")
print(f"\tNumber {len(concate)} is the length of the strings")

print(concate[0])
print(concate[1])
print(concate[2])
print(concate[3])
print(concate[4])
print(concate[5])

print("\n\t --------- Clicing ----------\n")

print(concate[:16])
print(concate[5:])
print(concate[10:len(concate)])
print("--------- Negative Slicing -------\n")
print(concate[-15:])
print(concate[-15:-1])
print(concate[-15:-4])


print("\n ------------- string functions------------\n")
print(concate.endswith('python'))
print(concate.capitalize())
print(concate.replace('python','React'))
print(concate.find("python"))
print(concate.count("python"))


print("---------- Exercise Solution -----------\n")

name = input("Enter you name: ")
print(len(name))

str = ("@@###%$$$$$$$$$$$$$$")
print(str.count('$'))
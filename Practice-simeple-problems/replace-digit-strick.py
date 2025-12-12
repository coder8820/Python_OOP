s = input("Enter string: ")
result = ""

for ch in s:
    if ch.isdigit():
        result += "*"
    else:
        result += ch

print(result)

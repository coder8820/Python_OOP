d = {}
key = input("Enter key: ")

if key in d:
    d[key] += 1
else:
    d[key] = 1

print(d)

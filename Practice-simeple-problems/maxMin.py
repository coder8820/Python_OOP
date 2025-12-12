t = (10, 3, 25, 7, 9)

maximum = t[0]
minimum = t[0]

for n in t:
    if n > maximum:
        maximum = n
    if n < minimum:
        minimum = n

print("Max:", maximum)
print("Min:", minimum)

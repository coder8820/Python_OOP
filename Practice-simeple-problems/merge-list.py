a = [5, 2, 9]
b = [1, 3, 7]

merged = a + b

# Bubble sort
for i in range(len(merged)):
    for j in range(len(merged) - 1):
        if merged[j] > merged[j+1]:
            merged[j], merged[j+1] = merged[j+1], merged[j]

print("Sorted merged list:", merged)

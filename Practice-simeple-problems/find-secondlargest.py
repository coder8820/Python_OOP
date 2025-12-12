lst = [10, 50, 20, 40, 30]

largest = max(lst)
second = None

for n in lst:
    if n != largest:
        if second is None or n > second:
            second = n

print("Second largest:", second)

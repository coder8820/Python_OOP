s = input("Enter string: ")
is_pal = True

for i in range(len(s)):
    if s[i] != s[len(s)-1-i]:
        is_pal = False
        break

print("Palindrome" if is_pal else "Not Palindrome")

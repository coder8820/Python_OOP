age = 18

if(age<=15):
    print('you are not allow to Drive a car')
elif(age==18):
    print("You are Allowed")
else:
    print("You are Welcome,appreciate it")

print("------------------ Trafic Light -------------")

light = "Yellow"
if(light == "red"):
    print("stop")
elif(light == 'green'):
    print('continue')
else:
    print("waiting State")


print(' ------- Grade student based on marks --------')

marks = 70
# marks = int(input("Enter you marks: "))

if(marks >= 90):
    print("Grade A")
elif(marks >= 80 and marks < 90):
    print('Grade is B')
elif(marks >= 70 and marks < 80):
    print('Grade is C')
elif(marks >= 60 and marks < 70):
    print("Grade is D")
else:
    print("I'm sorry, you have to try again")


print("------------------------ Exercise Nested if conditions -----------------\n")

age = 80

if(age >= 18):
    if(age >= 70):
        print("it's Riscky man, You can not drive")
    print("You can Drive")
elif(age < 18):
    print('come when your age become 18+')
else:
    print("let me see your status")
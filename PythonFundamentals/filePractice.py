# with open("practice.txt", 'w') as f:
#     f.write("He everyone\nWe are learning File I\O \nusing Java\nI like programming in Java")
#     f.close()

# with open("practice.txt", 'r') as f:
#     data = f.read()
#     new_data = data.replace("Java", "Python")
#     print(new_data)
#     f.close()



#  Replacing Data with data like (java to python)

# with open("demo.txt",'r') as f:
#     data = f.read()
#     newdata = data.replace("React js", "flutter development")
#     print(newdata)
#     f.close()


#  finding a data 

# word = "Java"
# def check_for_word(data):
#     with open("practice.txt", 'r') as f:
#         data = f.read()
#         if(data.find(word) != -1):
#             print("Found the Word")
#         else:
#             print("Searching word not found")
#         f.close()

# check_for_word(word)

def check_for_line():
    word = 'Java'
    data = True
    line_no =1
    with open("practice.txt", 'r') as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
            else:
                print("not found")
            line_no += 1
        f.close()
    return -1
check_for_line()

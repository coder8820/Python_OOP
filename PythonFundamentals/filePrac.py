# with open("demo2.txt", 'r') as f:
#     data = f.read()
#     # print(data)
#     count = 0
#     num = data.split(',')
#     print(num)
#     for val in num:
#         if(int(val)%2 == 0):
#             print("Even Number is ",val)
#             count += 1
#         else:
#             print("Odd Number is ",val)
    
# print("Total count of Even Uumber is ",count)

with open("demo2.txt", 'r') as f:
    data = f.read()
    print(data)
    num = data.split(',')
    print(num)
    count = 0
    for i in num:
        if int(i) % 2 == 0:
            print("Even Number is ", i)
            count += 1
print("Total count of Even Number is ", count)


    # num = ''
    # for i in range(len(data)):
    #     if data[i] == ',':
    #         print(int(num))
    #         num = ''
    #     else:
    #         num += data[i]
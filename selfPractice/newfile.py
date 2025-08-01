# try:
#     a = input("enter the number 1:")
#     b = input("enter the number 2:")
#     res = b/a
#     print(res)
# except Exception as e:
#     print(e)
# else:
#     print("no exception")    

# import json
# FILE = "data.json"

# print(type(FILE))
# # print(FILE[0])
# # print(FILE[1])
# with open(FILE, "r") as data:
#         print(data)
#         jsonData = json.load(data)
#         print(jsonData)






import json
FILE = "data.json"

print(type(FILE))

with open(FILE, "r") as writeData:
        jsonData = json.load(writeData)
        jsonData.append({"name": "komal", "age": 22})
        print(jsonData)

with open(FILE, "w") as d:   
        json.dump(jsonData, d)
        print("data added successfully")     
# 1. ZeroDivisionError
try:
    x = 10
    y = 0
    result = x / y
except ZeroDivisionError:
    print("Resolved: Division by zero is not allowed. Setting result = 0.")
    result = 0
print("Result:", result)


# 2. ValueError
try:
    user_input = "abc"
    number = int(user_input)
except ValueError:
    print("Resolved: Cannot convert to integer. Using default value = 0.")
    number = 0
print("Number:", number)


# 3. KeyError
try:
    my_dict = {"name": "Komal"}
    age = my_dict["age"]
except KeyError:
    print("Resolved: 'age' key not found. Setting default age = 20.")
    age = 20
print("Age:", age)


# 4. IndexError
try:
    my_list = [1, 2, 3]
    value = my_list[5]
except IndexError:
    print("Resolved: Index out of range. Using last element.")
    value = my_list[-1]
print("Value from list:", value)


# 5. FileNotFoundError
try:
    with open("missingfile.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Resolved: File not found. Creating a new file with default content.")
    with open("missingfile.txt", "w") as file:
        file.write("This is a new file.")
    content = "This is a new file."
print("File content:", content)

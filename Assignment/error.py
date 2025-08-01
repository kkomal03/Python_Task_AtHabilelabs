try:
    # 1. ZeroDivisionError
    x = 10 / 0

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

try:
    # 2. ValueError
    num = int("abc")

except ValueError:
    print("Error: Invalid value for integer conversion.")

try:
    # 3. KeyError
    my_dict = {"name": "Komal"}
    print(my_dict["age"])

except KeyError:
    print("Error: Key not found in dictionary.")

try:
    # 4. IndexError
    my_list = [1, 2, 3]
    print(my_list[5])

except IndexError:
    print("Error: List index out of range.")

try:
    # 5. FileNotFoundError
    with open("missingfile.txt", "r") as file:
        content = file.read()

except FileNotFoundError:
    print("Error: File not found.")

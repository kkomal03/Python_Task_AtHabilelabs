from datetime import datetime
# 1.Write a program to check if a number is prime or not.
def prime_check():
    num = int(input("Enter a number: "))
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print("Not Prime")
                break
        else:
            print("Prime")
    else:
        print("Not Prime")



# 2. Print all numbers from 1 to N that are divisible by both 3 and 5.
def divisible_by_3_and_5():
    num = int(input("Enter a number: "))
    for i in range(1, num ):
        if i % 3 == 0 and i % 5 == 0:
            print(i)



# 3.Find the sum of all even numbers from 1 to 100.
def sum_of_even_numbers():
    sum = 0
    for i in range(1, 101):
        if i % 2 == 0:
            sum = sum + i
    print("Sum of even numbers:", sum)





# 4. Check if a given year is a leap year using if-else.
def check_leap_year():
    year = int(input("Enter a year: "))
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print("Leap Year")
    else:
        print("Not Leap Year")




# 5.Print the factorial of a number using a loop.
def factorial():
    num = int(input("Enter a number: "))
    fact = 1
    for i in range(2, num + 1):
        fact *= i
    print("Factorial:", fact)





# 6. Write a program to count the number of words in a string using a loop.
def count_words():
    newStr = str(input("Enter the string:"))
    word_count = 0
    for word in newStr.split():
        word_count += 1
    print("Word Count:", word_count)



# 7. Find the largest of three numbers using if-else.
def largest_of_three():
    num1 = int(input("enter first number:"))
    num2 = int(input("enter second number:"))
    num3 = int(input("enter third number:"))
    if (num1 > num2) and (num1 > num3):
        print("First Number is greater", num1)
    elif (num2 > num1) and (num2 > num3):
        print("Second number is greater", num2)
    else:
        print("third number is greater", num3)
 


# 8.Given a number 1-7, print the day of the week using match.
def print_day_of_week():
    day = int(input("Enter a number (1-7): "))
    match day:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Invalid day")





# 9. Write a program to reverse a number using a loop.
def reverse_number():
    num = int(input("Enter a number: "))
    reverse = 0
    while num > 0:
        reverse = reverse * 10 + num % 10
        num = num // 10
    print("Reversed number:", reverse)



# 10. Check whether a character is a vowel or consonant using match.
def check_vowel_or_consonant():
    char = input("Enter a single alphabet: ")
    if len(char) != 1 or not char.isalpha():
        print("Please enter a single alphabet character.")
    else:
        match char.lower():
            case 'a' | 'e' | 'i' | 'o' | 'u':
                print("It's a vowel.")
            case _:
                print("It's a consonant.")





# 11. Print the multiplication table of a number using a loop.
def multiplication_table():
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


# 12. Check if a number is positive, negative, or zero using if-else.
def check_number_sign():
    num = int(input("Enter a number: "))
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")



# 13.Write a program to calculate the average of numbers in an array using a loop.
def calculate_average():
    arr = [1, 2, 3, 4, 5]
    sum = 0
    for i in arr:
        sum += i
    avg = sum / len(arr)
    print("Average:", avg)







# 14 .Print Fibonacci series up to N terms using a loop.
def fibonacci_series():
    n = int(input("How many terms? "))
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()




# 15. Write a program to take a character input and print whether it is an alphabet, digit, or special character using if-else.

def check_character_type():
    char = input("Enter a character: ")
    if char.isalpha():
        print("Alphabet")
    elif char.isdigit():
        print("Digit")
    else:
        print("Special Character")





# 16.Given a month number, print the season (e.g., summer, winter) using switch-case.
def print_season():
    month = int(input("Enter the month (1-12): "))

    match month:
        case 12 | 1 | 2:
            print("Winter season")
        case 3 | 4 | 5:
            print("Spring season")
        case 6 | 7 | 8:
            print("Summer season")
        case 9 | 10 | 11:
            print("Autumn season")
        case _:
            print("Invalid month")        




# 17.Count the number of vowels in a given string using a loop and if-else.
def count_vowels():
    string = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    print("Number of vowels:", count)            




# 18.Write a simple calculator using switch-case for operations (+, -, , /).
def simple_calculator():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    match operator:
        case '+':
            print("Result:", num1 + num2)
        case '-':
            print("Result:", num1 - num2)
        case '*':
            print("Result:", num1 * num2)
        case '/':
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Division by zero")
        case _:
            print("Invalid operator") 





# 19.Print all elements in a list/array greater than a given value using a loop and if-else.
def print_greater_elements():
    numbers = [12, 7, 19, 3, 25, 8]
    value = int(input("Enter the value to compare: "))
    print("Elements greater than", value, "are:")
    for num in numbers:
        if num > value:
            print(num)







#20. Check if a given string is a palindrome using a loop and if-else
def check_palindrome():
    text = input("Enter a string: ")
    if text == text[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")



choice = input("Enter your choice (1-20): ")

match choice:
    case "1":
        start = datetime.now()
        prime_check()
        end = datetime.now()
        print("Time taken:", (end - start).total_seconds(), "seconds")
    case "2":
        start = datetime.now()
        divisible_by_3_and_5()
        end = datetime.now()
        print("Time taken:", (end - start).total_seconds(), "seconds")
    case "3":
        start = datetime.now()
        sum_of_even_numbers()
        end = datetime.now()
        print("Time taken:", (end - start).total_seconds(), "seconds")
    case "4":
        start = datetime.now()
        check_leap_year()
        end = datetime.now()
        print("Time taken:", (end - start).total_seconds(), "seconds")
    case "5":
        start = datetime.now()
        factorial()
        end = datetime.now()
        print("Time taken:", (end - start).total_seconds(), "seconds")
    case "6":
        start = datetime.now()
        count_words()
        end = datetime.now()
        print("Time taken:", (end - start).total_seconds(), "seconds")
    case "7":
        start = datetime.now()
        largest_of_three()
        end = datetime.now()
        print("Time taken:", (end - start).total_seconds(), "seconds")
    case "8":
        start = datetime.now()
        print_day_of_week()
        end = datetime.now()
        print("Time taken:", (end - start).total_seconds(), "seconds")
    case "9":
        start = datetime.now()
        reverse_number()
        end = datetime.now()
        print("Time taken:", (end - start).total_seconds(), "seconds")
    case "10":
        start = datetime.now()
        check_vowel_or_consonant()
        end = datetime.now()
        print("Time taken:", (end - start).total_seconds(), "seconds")
    case "11":
        start = datetime.now()
        multiplication_table()
        end = datetime.now()
        print("Time taken:", (end - start).total_seconds(), "seconds")
    case "12":
        start = datetime.now()
        check_number_sign()
        end = datetime.now()
        print("Time taken:", (end - start).total_seconds(), "seconds")
    case "13":
        start = datetime.now()
        calculate_average()
        end = datetime.now()
        print("Time taken:", (end - start).total_seconds(), "seconds")
    case "14":
        start = datetime.now()
        fibonacci_series()
        end = datetime.now()
        print("Time taken:", (end - start).total_seconds(), "seconds")
    case "15":
        start = datetime.now()
        check_character_type()
        end = datetime.now()
        print("Time taken:", (end - start).total_seconds(), "seconds")
    case "16":
        start = datetime.now()
        print_season()
        end = datetime.now()
        print("Time taken:", (end - start).total_seconds(), "seconds")
    case "17":
        start = datetime.now()
        count_vowels()
        end = datetime.now()
        print("Time taken:", (end - start).total_seconds(), "seconds")
    case "18":
        start = datetime.now()
        simple_calculator()
        end = datetime.now()
        print("Time taken:", (end - start).total_seconds(), "seconds")
    case "19":
        start = datetime.now()
        print_greater_elements()
        end = datetime.now()
        print("Time taken:", (end - start).total_seconds(), "seconds")
    case "20":
        start = datetime.now()
        check_palindrome()  # ✅ Fixed: you were calling check_character_type() again
        end = datetime.now()
        print("Time taken:", (end - start).total_seconds(), "seconds")
    case _:
        print("Invalid choice.")

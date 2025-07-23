#1. Write a program to check if a number is prime or not.


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











# 2.Print all numbers from 1 to N that are divisible by both 3 and 5.




num = int(input("Enter a number: "))
for i in range(1,num):  
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        
   





# 3.Find the sum of all even numbers from 1 to 100.



sum = 0
for i in range (1,100):
    if(i % 2 == 0):
        sum = sum + i
print(sum)










# 4.Check if a given year is a leap year using if-else.



num = int(input("enter the year:"))
if num % 4 == 0:
    print ("Leap Year")
else:
    print("Not A Leep Year")    




# 5.Print the factorial of a number using a loop.


fact = 1
num = int(input("enter the number:"))
for i in range (2, num+1):
    fact = fact * i
   
print(fact)   




# 6.Write a program to count the number of words in a string using a loop.


newStr = "Hello In Python Using Loop"
word_count = len(newStr.split())
print(word_count)


newStr = str(input("Enter the string:"))
word_count = 0
for word in newStr.split():
    word_count += 1
print("Word Count:", word_count)










# 7.Find the largest of three numbers using if-else.


num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
num3 = int(input("enter third number:"))
if (num1 > num2) and (num1 > num3):
    print("First Number is greater", num1)
elif (num2 > num1) and (num2 > num3):
    print("Second number is greater", num2)
else:
    print("third number is greater", num3)  









# 8.Given a number 1-7, print the day of the week using switch-case.


day = int(input("Enter the day:"))
match day:
    case 1:
        print("Today is monady") 
    case 2:
        print("Today is tuesday")    
    case 3:
        print("Today is wednesday")   
    case 4:
        print("Today is thusday")   
    case 5:
        print("Today is friday")  
    case 6:
        print("Today is saturday")   
    case 7:
        print("Today is sunady")  
    case _:
        print("This number in not range of weeks")                          








# 9.Write a program to reverse a number using a loop.


num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10        
    reverse = reverse * 10 + digit 
    num = num // 10          

print("Reversed number:", reverse)






# 10.Check whether a character is a vowel or consonant using switch-case.


char = input("Enter a single alphabet: ")

if len(char) != 1 or not char.isalpha():
    print("Please enter a single alphabet character.")
else:
    match char.lower():
        case 'a' | 'e' | 'i' | 'o' | 'u':
            print("It's a vowel.")
        case _:
            print("It's a consonant.")




# 11.Print the multiplication table of a number using a loop.

num = int(input("Enter a number: "))

print(f"Multiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")



# 12.Check if a number is positive, negative, or zero using if-else.

num = int(input("Enter the number:"))
if num > 0 :
    print("number is positive")
elif num < 0:
    print("number is negative")
else:
    print("number is zero")        



# 13.Write a program to calculate the average of numbers in an array using a loop.


avg = 0
sum =0 
list = [1,2,3,4,5]
for i in list:
    sum = sum + i
    avg = (avg + sum)/len(list)
print("average of list :", avg)    


#14. Print Fibonacci series up to N terms using a loop.


n = 10
a = 0
b = 1
for i in range(n):
    print(a)
   
    temp = a
    a = b
    b = temp + b






# 15.Write a program to take a character input and print whether it is an alphabet, digit, or special character using if-else.


newString = input("Enter the string:")

if ('a' <= newString <= 'z') or ('A' <= newString <= 'Z'):
    print("Alphabet")
elif '0' <= newString <= '9':
    print("Digit")
else:
    print("Special Character")



##using inbuilt function
if newString.isalpha():
    print("Alphabet")
elif newString.isdigit():
    print("Digit")
else:
    print("Special Character")





# 16.Given a month number, print the season (e.g., summer, winter) using switch-case.



month = int(input("Enter the month (1-12): "))

match month:
    case 12 | 1 | 2:
        print("Winter season")
    case 3 | 4:
        print("Spring season")
    case 5 | 6 | 7 | 8:
        print("Summer season")
    case 9 | 10 | 11:
        print("Autumn season")
    case _:
        print("Invalid month")



\



# 17.Count the number of vowels in a given string using a loop and if-else.



string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in string:
    if char in vowels:
        count += 1

print("Number of vowels:", count)




# 18.Write a simple calculator using switch-case for operations (+, -, , /).



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


numbers = [12, 7, 19, 3, 25, 8]
value = int(input("Enter the value to compare: "))
print("Elements greater than", value, "are:")
for num in numbers:
    if num > value:
        print(num)




# 20.Check if a given string is a palindrome using a loop and if-else


string = input("Enter a string: ")
length = len(string)
is_palindrome = True

for i in range(length // 2):
    if string[i] != string[length - i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

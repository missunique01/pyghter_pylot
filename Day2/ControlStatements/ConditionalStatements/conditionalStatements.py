# Conditional Statements
#if , if else, elif

# Exapmle 1 --Lets write a program to print a person is eligible for vote or not
age = int(input("Please enter your age: "))
if age >= 18:
    print("Eligible for vote")
else:
    print("Not eligible for vote")

#Example 2

if True:
    print("True Condition")
else:
    print("False Condition")

#Example 3

if 1:
    print("one")
else:
    print("zero")
if 0:
    print("one")
else:
    print("zero")

# Example 4 find a number is odd or even

# Approach1
num = int(input("Enter a number "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd Number")
#Approach2 using ternary operator
print("Even number ") if num %2 == 0 else print("Odd number")

# Example 5 - If else -- Multiple statements in a single line
number = int(input("Enter a Number "))
{print("hello"), print("Python")} if num >= 20 else {print("hi"), print("Java")}

# Example 6 - Elif Printing week names using week numbers
weekNum = int(input("Enter a weekno"))
if weekNum == 1:
    print("Sunday")
elif weekNum == 2:
    print("Monday")
elif weekNum == 3:
    print("Tuesday")
elif weekNum == 4:
    print("Wednesday")
elif weekNum == 5:
    print("Thursday")
elif weekNum == 6:
    print("Friday")
elif weekNum == 7:
    print("Saturday")
else:
    print("Not a valid weeknum")
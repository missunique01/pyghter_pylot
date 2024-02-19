# Taking input from user

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print(num1)
print(num2)
print(type(num1)) # Type will be str because we are using input() fu
print(type(num2))

print(num1+num2) # Here concatenation is happening

#Approach 1

num3 = int(input("Enter first number: "))
num4 = int(input("Enter second number: "))

print(num3)
print(num4)
print(type(num3)) # Type will be str because we are using input() fu
print(type(num4))

print(num3+num4) # Here concatenation is happening

# Approach 2 -- Converting the function of Num1 & Num2 to int at the time of print & COncating
print(int(num1) + int(num2))

# Approach 3 using decimal numbers

num5 = input("Enter a decimal number")
num6 = input("Enter a decimal number")
print(type(num5))
print(type(num6))
print(num5 + num6)
print(float(num5) + float(num6))
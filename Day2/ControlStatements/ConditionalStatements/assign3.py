# Check the largest of 3 numbers

num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1>= num2 and num1 >= num3:
    print("Largest number is ", num1)
elif num2 > num1 and num2 > num3:
    print("Largest number is ", num2)
else:
    print("Largest number is", num3)
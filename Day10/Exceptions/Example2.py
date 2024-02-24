#Example2

print("this is the start of program")
print("Program in progress")
print(10/5) #2.0
try:
    print(10/0)  #ZeroDivisionError: division by zero
except ZeroDivisionError: #Specifying the error with name
    print("Number is not divisible by 0")
print("program completed")
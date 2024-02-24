#Raising our own exceptions

def m1(num):
    if num<0:
        raise ValueError("Only integers are allowed")
    if num%2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
num = int(input())
try:
    m1(num)
except ValueError:
    print("ValueError exception occured & Handled")
print("Program completed")


#Multiple Except blocks -- try, except, else, finally
#The exceptions block will execute only when there is an exception occured
#else block will execute if no exception is occured
#Finally block will execute always
num1, num2 = 5,10
result = num1/num2
print("Result is : ",result) #this is positive case
#----------------------------------------------------Negative case------------
try:
    num3 = int(input("Enter a Number "))
    num4 = int(input("Enter a number "))
    res = num3/num4
    print("Result is :", res)
except ZeroDivisionError:
    print("Thrown Zerodivisionerror Exception ")
except SyntaxError:
    print("Thrown Syntax error Exception")
except:
    print("Exception handled")
else:
    print("No exception occured")
finally:
    print("Finally block executes always")



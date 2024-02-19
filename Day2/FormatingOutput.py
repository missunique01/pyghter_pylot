# Formatting output in Python

name = "John"
age = 30
salary = 30000

name, age, salary = "John", 30, 30000
# Approch 1 for printing
print(name)
print(age)
print(salary)
# Approach 2 for printing
print(name, age, salary) # to print three values in a Single line

# Approach3 for printing along with some message
print("Name is", name)
print("Age is ", age)
print("Salary is ", salary)

# Approach4 for printing along with some message in a single line
# USing % symbol
print("Name is:%s  , Age is:%d  , Salary is:%g " %(name, age, salary))
# Approach 5 using { }
print("Name is:{}  , Age is:{}  , Salary is:{} " .format(name, age, salary))

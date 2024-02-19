# range() function in python
# it prints values between the range
# range(10) 0 to 9
# range(1, 10) means 1,2,3,4,5,5,6,7,8,9
# range(1,10,2) means starting 1, ending 10 and increment by 2

print(range(10))
print(list(range(10)))
print(list(range(5,10)))

# Print odd numbers between 1 to 10
print(list(range(1,10,2)))

# Print only even numbers between 1 to 10
print(list(range(2,10,2)))

# printing numbers between 10 - 1
print(list(range(10,1,-1)))
#printing numbers betweeen -10 to -5
print(list(range(-10,-5)))
#printing numbers betweeen -10 to -5 increment by 2
print(list(range(-10,-5,2))) #10,-8,-6
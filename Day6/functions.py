#Example 1 - Creating a function
#def is keyword used to define a function
#we need to call the function to print or use the function
def myfunction():
    print("Hello")
myfunction() #Calling the function

#Example 2 - FUnction with single argument
def myfuntwo(name):
    print("Hello", name)
myfuntwo("Nazma")

#Example 3 - FUnction with multiple arguments
def myfunthree(a,b):
    return  (a+b)
sum = myfunthree(4,5)
print(sum)
print(myfunthree(6,8)) #it will call the function & Return the answer & Prints

#Example4 - Creating a empty function and printing it
def myfunctionfour():
    return
print(myfunctionfour())

#Example 5 - create a function withour any return then will get None
def myfuncfive():
    i = 10
print(myfuncfive())

#Example 6 - creating a function with 2 arguments & write print statement & Calling
def myfuncsix(a,b):
    print(a+b)
myfuncsix(2,4) #if we wrote the print() fucntion at function itslef then func calling is enough







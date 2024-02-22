#Example 1 -- Define function and expecting 2 arguments
def func(i,j):
    print(i,j)
func(2,3)  #Positional arguments
func(j=20,i=10) #keyword arguments

#Example2 - Assigning default values to positional arguments
def functwo(i,j=10):
    print(i,j)
functwo(20) #PAssing only one value because we have already assigned a default,
# If you dont want to print the default value then we can pass two arguments
functwo(300,310)

#Example3 - Keyword arguments
def functhree(name,greetmsg):
    print(greetmsg + " "+ name)

functhree(name = "John", greetmsg= "Hello")
functhree(greetmsg= "Hello",name = "John")

#Example4 --
def myfunctfour(a,b,c):
    print(a,b,c)
myfunctfour(10,20,30)  #positional parameters
myfunctfour(b=40, a= 50,c=60) #Keyword parameters

#Example 5 -- Functions returns multiple values
def myfuncfive(a,b):
    if a>b:
        return a,b
    else:
        return b,a
print(myfuncfive(10,20))
print(myfuncfive(100,90))
res = myfuncfive(500,490)
print(res)

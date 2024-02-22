#Example1
global_var = 20 #Global Variable

def myfunc():
    local_var = 30 #Local Variable
    print(global_var)
    print(local_var)
myfunc()

#Example2 -
xy = 100  #Global var
def cool():
    xy = 200 #Local var
    print(xy)
cool()  #Prints local variable
print(xy) #Prints global variable value

#Example3 -- Modifying a global variable inside a funciton & printing
global_xy = 100
def myfuncthree():
    global global_xy
    xy_glo_fun = 500  #GLobal variable
    print(xy_glo_fun)
myfuncthree()

#Example 4 -
x = 100
def myfunctionfour():
    global x
    x = 200
    print(x)
myfunctionfour()  #200
print(x) #200
#Example 5 -
y = 100
def mufunctionfive():
    global y
    y = 200
    print(x)
print(y) #Will get 100 because we are not calling the function

#Example 6 - defining a variable as global inside the funciton without having the gloabl variable
#global can be created inside the funciton to do that we need to use global keyword
#We can access this global variable outside the function
def myfuncsix():
    global z_six
    z_six = 110
    print(z_six)
myfuncsix()
print(z_six)

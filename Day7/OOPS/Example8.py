#Example 8 -- Creating / Using a constructor

class MyClass:
    def __init__(self): #Default constructor
        print("This is constructor")
    def m1(self):
        print("This is method one")
    def m2(self,x,y):
        return (x+y)
mc = MyClass()  #Invokoed constructor automatically
mc.m1()  #Invoking the method explicitly by using object
res = mc.m2(10,20)
print(res)
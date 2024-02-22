#Example 3 Creat a class and a method
class MyClass:
    def m1(self):
        print("Instance Method")
    @staticmethod
    def m2(self,num):
        print(self,num)
myclass_obj = MyClass()
myclass_obj.m1() #Calling the instance method using object
MyClass.m2(110,100)  #Calling the static method using class name
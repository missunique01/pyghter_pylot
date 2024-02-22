#Example creating a a class
#Self means the method is belongs to that particular function
class MyClass:
    def myfunc(self):
        pass
    def display(self,name):
        print(name)
mcObject = MyClass() #Object for the class
print(mcObject.myfunc())  #Instance methods (We are able to call it using object)
print(mcObject.display("Nazma"))


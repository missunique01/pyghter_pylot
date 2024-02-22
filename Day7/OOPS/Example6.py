#Combination of global, class & Local Variables using same variable names
#To access the gloabal variables which is having same name as local variables
# then we need to use globals() fucntion
a,b = 2,4 #Global Variables
class MyClass:
    a,b = 10,20 #Class Variables
    def add(self,a,b): #Local Variables
        print(a+b) #Local Variables accessing
        print(self.a + self.b) #Accesing Class Variables
        print(globals()["a"] + globals()["b"]) #Accesing global variables
mc = MyClass()
mc.add(40,50)


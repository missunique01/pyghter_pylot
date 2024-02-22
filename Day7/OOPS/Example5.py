#Combination of global, class & Local Variables
i,j = 2,4 #Global Variables
class MyClass:
    a,b = 10,20 #Class Variables
    def add(self,x,y): #Local Variables
        print(x+y) #Local Variables accessing
        print(self.a + self.b) #Accesing Class Variables
        print(i+j) #Accesing global variables
mc = MyClass()
mc.add(40,50)


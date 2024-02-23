#
class A:
    a,b = 50,40 #Class Variables
class B(A):
    i,j = 100,90 #Class Variables
    def m(self,x,y): #Local Variables
        print(x+y)
        print(self.i + self.j) #Accessing class variables
        print(self.a + self.b)
b_obj = B()
b_obj.m(2,3)
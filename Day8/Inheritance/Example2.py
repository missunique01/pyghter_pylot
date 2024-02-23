#Example 2
# --- Single Inheritance ---------
class A:
    x,y = 10,20 #Class Variables
    def m1(self):
        print(self.x + self.y) #Accessing class variables using self keyword
class B(A):
    i,j = 60,50 #Class Variables
    def m2(self):
        print(self.i - self.j) #Accessing class variables using self keyword
b_obj = B()
b_obj.m2()
b_obj.m1()
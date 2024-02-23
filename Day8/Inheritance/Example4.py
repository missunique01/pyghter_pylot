# -------------- Hierarchy Inheritance-------------

class A:
    x,y = 20,10
    def m1(self):
        print(self.x+self.y)
class B(A):  #B is A's Child
    i,j = 40,30
    def m2(self):
        print(self.i-self.j)
class C(A): #C is A's Child
    a,b = 2,3
    def m3(self):
        print(self.a * self.b)
b_obj = B() #Object created & we wan access only B class & A class Methods
b_obj.m2()
b_obj.m1()
c_obj = C() #Object created & we wan access only C class & A class Methods
c_obj.m3()
c_obj.m1()
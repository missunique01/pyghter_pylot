# --------------MULTIPLE INHERITANCE --------------------------
# 2 parent classes and 1 child class
class A:
    x,y = 20,30
    def m1(self):
        print(self.x + self.y)
class B:
    i,j = 50,40
    def m2(self):
        print(self.i - self.j)
class C(A,B):  #C is child of A,B
    a,b = 2,3
    def m3(self):
        print(self.a*self.b)

c_obj = C() #Created a C class obj & Now able to acces A class, B class methods 
c_obj.m3()
c_obj.m2()
c_obj.m1()
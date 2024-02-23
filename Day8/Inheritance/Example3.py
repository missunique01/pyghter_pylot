#----------------MULTILEVEL INHERITANCE-------------
#It is a combination of multilevel inheritance

class A:
    x,y = 30,40
    def m1(self):
        print(self.x+self.y)
class B(A):
    i,j = 60,50
    def m2(self):
        print(self.i -self.j)
class C(B):
    a,b = 2,3
    def m3(self):
        print(self.a*self.b)
c_obj = C()  #Able to access m1(),m2(),m3() methods
b_obj = B() #Able to access m1(),m2() Methods
a_obj = A() #Able to access m1() Method
c_obj.m3()
c_obj.m2()
b_obj.m2()
b_obj.m1()
a_obj.m1()

#Creating a simple inheritance program
# ---SINGLE INHERITANCE-----
class A:
    def m1(self):
        print("This is m1 method from class A")
class B(A): #B becomes A class child
    def m2(self):
        print("This is method m2 from class B")
a_obj = A()
b_obj = B()
b_obj.m1()
b_obj.m2()
a_obj.m1()
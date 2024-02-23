# Method Overriding
#Writing same method in the child class
#Super is keyword which will refer the parent class
#calling parent class method using child class (super())
class A:
    def m1(self):
        print("This is m1 method from A class")
class B(A):
    def m1(self): #M1 method id overriding
        print("This is m1 method from B class")
        super().m1() # to invoke the parent class method using child class
b_obj = B()
b_obj.m1() #B class m1 method is getting accessed & if we use super() then will get the A class m1 method
# output aswell
#Example4
#Local Variables & Global Variables
#One more Variable is Class Variable
class Myclass:
    a,b = 10,20 #Class Variables created because there are created inside the class
    def add(self):
        print(self.a+self.b)
    def mul(self):
        print(self.a*self.b)
mc = Myclass()
mc.add()
mc.mul()
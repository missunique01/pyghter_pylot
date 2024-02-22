#Example 9 - Passing arguments to constructor
class Myclass:
    name = "John"
    def __init__(self,name):  #Paramaterized constructor
        print(name)
        print(self.name)
mc = Myclass("David") #Passing parameter to the constructor
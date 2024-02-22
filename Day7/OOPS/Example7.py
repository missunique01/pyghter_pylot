#Creating multiple objects for a single class
class Myclass:
    def display(self,name):
        print("This is display method")
        print(name)

obj1 = Myclass()
obj2 = Myclass()
obj1.display("nazma")
obj2.display("Asma")



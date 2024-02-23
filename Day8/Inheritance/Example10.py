# EXample -1 --METHOD OVERLOADING
class Human:
    def sayHello(self, name = None):
        if name is not None:
            print("Hello "+name)
        else:
            print("Hello")
human_obj = Human()
human_obj.sayHello("Nazma")  #Passing parameter
human_obj.sayHello() #Without passing parameter


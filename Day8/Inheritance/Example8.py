# OVERRIDING VARIABLES
class PARENT:
    name = "Asma" #Class Variables
class CHILD(PARENT):
    name = "Nazma" #Class Variables & Over riding the variable
    def test(self):
        print(super().name) #Accesing parent class variable &Printing
child_obj = CHILD()
print(child_obj.name)
child_obj.test()
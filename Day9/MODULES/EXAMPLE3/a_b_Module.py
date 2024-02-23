#Access a,b modules
#Approach1
import b
from Day9.MODULES.EXAMPLE3 import a

a_obj = a.Animal()
b_obj = b.Bird()
a_obj.display()
b_obj.display()

#Approach2
from Day9.MODULES.EXAMPLE3.a import Animal
from b import Bird
a_obj1 = Animal()
b_obj1 = Bird()
a_obj1.display()
b_obj1.display()
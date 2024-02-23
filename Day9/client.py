#Import sys and add the package path and change the '\' to '/' slashes
import sys
sys.path.append("C:/Users/home/PycharmProjects/PythonTrainingProject/Day9/Pack1")
#Approach1
import module1
import module2
module1.display()
module2.show()

#Approach2 - in this approach no need to use module name to call the function
from module1 import *
from module2 import *
display()
show()
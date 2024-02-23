#Scenario2 --
#created package1 - then created one module
#Then created package2 inside package1 -then created another module
import sys
sys.path.append("C:/Users/home/PycharmProjects/PythonTrainingProject/Day9/package1")
sys.path.append("C:/Users/home/PycharmProjects/PythonTrainingProject/Day9/package1/package2")
#Approach1
import module1
import module2
module1.display()
module2.show()
#Approach2
from module1 import *
from module2 import *

display()
show()
#Call the funcitons from Animal & Bird Modules
#Approach1
from Day9.MODULES.EXAMPLE2 import Animal_Module as AM
import  Bird_Module as BM

AM.fly()
AM.color()
BM.fly()
BM.color()

#Approach2
from Day9.MODULES.EXAMPLE2.Animal_Module import *
fly()
color()
from Bird_Module import *
fly()
color()
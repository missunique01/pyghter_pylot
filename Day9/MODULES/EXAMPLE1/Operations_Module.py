#Operations Module
#To access a module import it using import keyword
#To access the functions use module.<<function name>>
# Approach1
from Day9.MODULES.EXAMPLE1 import Calculator_Module

Calculator_Module.add(100, 200)  #300
Calculator_Module.mul(2, 3) #6
#Approach2
from Day9.MODULES.EXAMPLE1.Calculator_Module import add,mul
add(100,200) #300
mul(2,3) #6
#Approach3
from Day9.MODULES.EXAMPLE1.Calculator_Module import *
add(2,6) #8
mul(1,3) #4
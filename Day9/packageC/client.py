import sys
sys.path.append("C:/Users/home/PycharmProjects/PythonTrainingProject/Day9/packageA")
sys.path.append("C:/Users/home/PycharmProjects/PythonTrainingProject/Day9/packageB")

#Approach1
import EMP_Module
import STU_Module
emp_obj = EMP_Module.Employee(112015,"Naina",450000)  #give module name dot class name if our constructor is params then param
stu_obj = STU_Module.Student(100,"Parveen",90)
emp_obj.displayemp()
stu_obj.displaystu()

#Approach2
from EMP_Module import *
from STU_Module import *
empobj = Employee(112054,"Mumtaaj",50000)
empobj.displayemp()
stuobj = Student(101,"Nissy",92)
stuobj.displaystu()
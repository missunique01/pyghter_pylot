#Example 10 -- Creating a class Employee, Create one constructor
# which will accept three parameters(eid,ename, esale)
#Display() method print eid,ename, &esal
class emp:
    def __init__(self,eid,ename,esal):
        self.eid = eid
        self.ename = ename
        self.esal = esal
    def display(self):
        print(self.eid,self.ename,self.esal)
emp_obj = emp(100,"Nazma",40000) #Creating the object &the contructor will be invoked &passing params
emp_obj.display()
emp_obj2 = emp(101,"Asma",40000) #Creating the object &the contructor will be invoked &passing params
emp_obj2.display()
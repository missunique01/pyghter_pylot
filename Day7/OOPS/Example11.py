#Example 10 -- Creating a class Employee, Create one constructor
# which will accept three parameters(eid,ename, esal)
#Creating another constructor to print the eid,ename,esal
class emp:
    def __init__(self,eid,ename,esal):
        self.eid = eid
        self.ename = ename
        self.esal = esal
    def __str__(self):
        return self.ename
e1 = emp(101,"Nazma",50000)
print(e1)
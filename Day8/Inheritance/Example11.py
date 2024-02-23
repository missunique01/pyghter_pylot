#Example - 2 for OVERLOADING
class Calculation:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)
cal_obj = Calculation()
cal_obj.add() #withour parameters
cal_obj.add(2,3) #Passing only 2 arguments
cal_obj.add(10,20,30)
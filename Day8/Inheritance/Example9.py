# ---------METHOD OVERRIDING------------
#Heirarchy Inheritance
class Bank:
    def rateofinterest(self):
        return 0
class XBank(Bank):
    def rateofinterest(self):
        return  10
class YBank(Bank):
    def rateofinterest(self):
        return 12

x_obj = XBank() #Created object for x Bank Class
print(x_obj.rateofinterest()) #Calling/invoking the method using obj & Printing
y_obj = YBank() #Created object for Y Bank Class
print(y_obj.rateofinterest()) #Calling/invoking the method using obj & printing

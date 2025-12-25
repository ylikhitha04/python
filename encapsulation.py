class AccountHolder:
    def __init__(self):
        self.AccountHolder=123456
        self.__balance=3456
        self.__password=123
    def setpassword(self,p):
        self.__password=p
    def getpassword(self):
        return self.__password
    def getbalance(self):
        return self.__balance
a=AccountHolder()
print(a.getbalance())
print(a.getpassword())
    

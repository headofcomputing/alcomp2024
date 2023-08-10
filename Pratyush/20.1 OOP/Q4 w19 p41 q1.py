class PrintAccount():
    #question i
    def __init__(self,FirstName,LastName,PrintID):
        self.__firstName=FirstName
        self.__lastName=LastName
        self.__printID=PrintID
        self.__credits=50

    #question ii
    def SetFirstName(self,name):
        self.__firstName=name
    
    #question iii
    def GetName(self):
        return self.__firstName+" "+self.__lastName
    
    #question iv
    def AddCredits(self,moneyInput):
        bonus=0
        '''markscheme reccomends constants like CreditPerDollar = 25
        FreeCredit10 = 25
        FreeCredit20 = 50
        Twenty = 20
        Ten = 10 '''
        bought=moneyInput*25
        if moneyInput>=20:
            bonus=50
        elif moneyinput>=10:
            bonus=25
        self.__credits=self.__credits + bought + bonus

    
#StudentAccount : ARRAY[0,999] OF PrintAccount
studentAccount=[None]*1000

    
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
    
    #for question vi
    def GetPrintID(self):
        return self.__printID
    
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
        elif moneyInput>=10:
            bonus=25
        self.__credits=self.__credits + bought + bonus

    
#question v
# StudentAccount : ARRAY[0,999] OF PrintAccount
studentAccount=[None]*1000
for i in range(0,1000):
    studentAccount[i]=PrintAccount("Bingus","Frog","bilsmi1")



#question vi

def CreateID(fName,lName):
    def findEmpty():
        emptyCounter=0
        empty=False
        while empty==False and emptyCounter<=999:
            if studentAccount[emptyCounter] == None:
                empty==True
                return emptyCounter
            else:
                emptyCounter=emptyCounter+1
        if empty==False:
            return -1
    
    def checkName(name):
        found=False
        counter=0
        while found==False and counter<=999:
            if studentAccount[counter].GetPrintID() == name:
                found=True
            else:
                counter=counter+1
        return found

    
    
    increment=1

    done=False
    printID=fName[:3]+lName[:3]+str(increment)
    
    #if its not in the list
    if checkName(printID)==False:
        studentAccount[findEmpty()]=PrintAccount(fName,lName,printID)
    else:
        increment=increment+1
        



            

CreateID("bill","sbith")

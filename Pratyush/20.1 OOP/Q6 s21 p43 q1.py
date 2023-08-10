
class foodItem: 
    #constructor        Question i
    def __init__(self,name,code,cost):
        self.__name=name
        self.__code=code
        self.__cost=cost

    #these were needed for question ii
    def getCode(self):    
        return self.__code
    
    def getCost(self):    
        return self.__cost

class vendingMachine:
    #constructor        Question i
    def __init__(self,item1,item2,item3,item4): #parameters should be type : foodItem
        self.__moneyIn=0 #moneyIn : INTEGER
        self.__items=[None]*4 #items: ARRAY[0,3] OF foodItem
        self.__items[0]=item1
        self.__items[1]=item2
        self.__items[2]=item3
        self.__items[3]=item4    

    #question ii
    def checkValid(self,code):
        flag=False
        count=0

        while count<=3 and flag==False: #checks if the object is in the vending machine
            if self.__items[count].getCode()==code:
                flag=True
            else:
                count=count+1

        if flag==False: #if it isnt, returns -1
            return -1
        elif self.__moneyIn<self.__items[count].getCost(): #if money in is not met
            return -2
        else: #everything ok, return index
            return count
        
bread=foodItem("Bread",123,5)    
store=vendingMachine(bread,bread,bread,bread)
print(store.checkValid(123))

#Question iii
machineOne=vendingMachine(chocolate,sweets,sandwich,apple)


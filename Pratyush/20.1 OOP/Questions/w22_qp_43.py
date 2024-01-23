class Card():
    #number as Integer
    #color as String
    def __init__(self,number,color): 
        self.__number=number 
        self.__color=color 

    def getColor(self):
        return self.__color
    
    def getNumber(self):
        return self.__number

c1=Card(1,'red')
c2=Card(2,'red')

class Hand():
    #all c1 - c5 parameters of type Card
    #firstCard as integer
    #numbercard as integer
    def __init__(self,c1,c2,c3,c4,c5):
        self.__cards=[c1,c2,c3,c4,c5]
        self.__firstCard=0
        self.__numberCards=5
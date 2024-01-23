#question a
'''Properties are private because
this keeps the data more secure
only the object itself can access its data
???'''

#question b
class Cards():
    def __init__(self,number,shape):
        if number>=0 and number<=9:
            if shape=="square" or shape=="triangle" or shape=="circle":
                self.__number=number
                self.__shape=shape
            else:
                print("invalid shape")
        else:
            print("invalid number")
    #question c
    def getNumber(self):
        return self.__number
    
    def getShape(self):
        return self.__shape
    
    #question d
OneS=Cards(1,"square")

TwoT=Cards(2,"triangle")

#question e
def Compare(card1,card2):
    if card1.getShape()==card2.getShape() and card1.getNumber()==card2.getNumber():
        print("SNAP")
        return -1
    else:
        if int(card1.getNumber())>=int(card2.getNumber()):
            return card1.getNumber()
        else:
            return card2.getNumber()
        
print(Compare(OneS,OneS))


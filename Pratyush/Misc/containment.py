class Cards():
    def __init__(self,number,shape):
        if number>=0 and number<=9:
            if shape.lower() =="square" or shape.lower()=="triangle" or shape.lower()=="circle":
                self.__number=number
                self.__shape=shape.lower()
            else:
                print("error with Shape input")
        else:
            print("error with number input")

    def GetNumber(self):
        return self.__number
    

OneS=Cards(1,"square")
Dulpicate=Cards(1,"square")

def Compare(card1,card2):
    if card1==card2:
        print("SNAP")
    else:
        print("diff")
        

Compare(OneS,Dulpicate)
a=Cards(1,"square")
class Character():
    def __init__(self,name,xPosition,yPosition):
        self.__Name=name            #self.__Name : String
        self.__XPosition=xPosition  #self.__XPosition : Integer
        self.__YPosition=yPosition  #self.__YPosition : Integer

    def GetXPosition(self):
        return self.__XPosition
    
    def GetYPosition(self):
        return self.__YPosition
    
    def SetXPosition(self,X):
        print("hello")
        X=X+self.__XPosition
        print(X)
        if X>10000:
            self.__XPosition=10000
        elif X<0:
            self.__XPosition=0
        else:
            self.__XPosition=X

    def SetYPosition(self,Y):
        Y=Y+self.__YPosition
        if Y>10000:
            self.__YPosition=10000
        elif Y<0:
            self.__YPosition=0
        else:
            self.__YPosition=Y

    def Move(self,direc): #string parameters up,down,left right
        if direc=="up":
            self.__YPosition +=10
        elif direc=="down":
            self.__YPosition -=10
        elif direc=="left":
            self.__YPosition -=10
        elif direc=="right":
            self.__YPosition +=10
        else:
            print("wrong input")

Jack=Character('Jack',50,50)


#c
class BikeCharacter(Character):
    def __init__(self,name,xPosition,yPosition):
        super().__init__(name,xPosition,yPosition)
    
    def Move(self,direc): #string parameters up,down,left right
        if direc=="up":
            super().SetYPosition(20)
        elif direc=="down":
            super().SetYPosition(-20)
        elif direc=="left":
            super().SetXPosition(-20)
        elif direc=="right":
            super().SetXPosition(20)
        else:
            print("wrong input")

Karla=BikeCharacter("Karla",100,50)
    
#Main
name=input("please enter the name of the character you want to move ").lower()
while name!='jack' and name!='karla':
    name=input("You can only enter Jack or Karla. Please re-enter name ").lower()

direction=input("enter direction you would like to move ").lower()
while direction!='up' and direction!='down' and direction!='left' and direction!='right':
    direction=input("please re-enter valid direction: up, down, left, or right only ").lower()

if name=="jack":
    Jack.Move(direction)
    print("Jack's new position is X=",Jack.GetXPosition()," Y=",Jack.GetYPosition())
else:
    Karla.Move(direction)
    print("Karla's new position is X=",Karla.GetXPosition()," Y=",Karla.GetYPosition())

            


    
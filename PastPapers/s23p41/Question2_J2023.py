class Vehicle():
    def __init__(self,pID,pMaxSpeed,pIncreaseAmount):
        self.__ID=pID #self.__ID : STRING
        self.__MaxSpeed=pMaxSpeed # self.__MaxSpeed : INTEGER
        self.__CurrentSpeed=0 #self.__CurrentSpeed : INTEGER
        self.__IncreaseAmount=pIncreaseAmount #self.__IncreaseAmount : INTEGER
        self.__HorizontalPosition=0 #self.__HorizontalPosition : INTEGER

    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    
    def GetMaxSpeed(self):
        return self.__MaxSpeed
    
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition
    

    def SetCurrentSpeed(self,speed):
        self.__CurrentSpeed=speed

    def SetHorizontalPosition(self,position):
        self.__HorizontalPosition=position

    
    def IncreaseSpeed(self):
        self.__CurrentSpeed += self.__IncreaseAmount
        if self.__CurrentSpeed>self.__MaxSpeed:
            self.__CurrentSpeed= self.__MaxSpeed
        self.__HorizontalPosition += self.__CurrentSpeed

#FOR Q c, under class Vehicle
    def OutputInfo(self):
        print("For vehicle with ID: ",self.__ID)
        print("Horizontal Position: ",self.__HorizontalPosition)
        print("Speed: ",self.__CurrentSpeed)


    

class Helicopter(Vehicle):
    def __init__(self,pID,pMaxSpeed,pIncAmount,pVerticalChange,pMaxHeight):
        super().__init__(pID,pMaxSpeed,pIncAmount)
        self.__VerticalChange=pVerticalChange #self.__VerticalChange : INTEGER
        self.__MaxHeight=pMaxHeight #self.__MaxHeight : INTEGER
        self.__VerticalPosition=0 #self.__VerticalPosition : INTEGER

    def IncreaseSpeed(self):
        self.__VerticalPosition += self.__VerticalChange
        if self.__VerticalPosition>self.__MaxHeight:
            self.__VerticalPosition= self.__MaxHeight
        super().IncreaseSpeed()

    #Wasnt sure about question C. vague.
    #for Q c, under class Helicopter
    def OutputInfo(self):
        super().OutputInfo()
        print("vertical position: ",self.__VerticalPosition)
        

#main program, d)
car=Vehicle("Tiger",100,20)
helicopter=Helicopter("Lion",350,40,3,100)
car.IncreaseSpeed()
car.IncreaseSpeed()
car.OutputInfo()
helicopter.IncreaseSpeed()
helicopter.IncreaseSpeed()
helicopter.OutputInfo()

#Took 30 minnutes to finish


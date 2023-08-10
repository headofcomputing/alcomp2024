class Player:
    #initialisation
    def __init__(self,playerID): #question i
        self.__score=0
        self.__category="Not Qualified"
        self.__pID=playerID

    #Getters    question ii
    def GetScore(self):
        return self.__score
    
    def GetCategory(self):
        return self.__category
    
    def GetPlayerID(self):
        return self.__pID
    
    #Setter     Question iii
    def SetPlayerID(self,playerID):
        while len(playerID)>15 or len(playerID)<4:
            playerID=input("please enter a valid Player ID")
        self.__pID=playerID
        print("Player ID successfully set")

    #set score  Question iv
    def SetScore(self,ScoreInput):
        if ScoreInput>=0 and ScoreInput<=150:
            self.__score=ScoreInput
            return True
        else:
            print("error: score value outside valid range")
            return False
        
    #set category   Question v
    def SetCategory(self):
        if self.__score>120:
            self.__category="Advanced"
        elif self.__score>80:
            self.__category="Intermediate"
        elif self.__score>=50:
            self.__category="Beginner"
        else:
            self.__category="Not Qualified"

#question vi
def CreatePlayer():
    playerID=input("what is your PlayerID? ")
    score=input("what is your score? ")
    JoannePlayer=Player(playerID)
    JoannePlayer.SetScore(int(score))
    JoannePlayer.SetCategory()
    print("your category is", JoannePlayer.GetCategory())

CreatePlayer()

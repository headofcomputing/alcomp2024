import random

class Character:
    def __init__(self,name): #constructor question A
        self.__name=name
        self.__skill=0
        self.__health=50
        self.__shield=random.randint(1,25)

    #getter Question b
    def getSkill(self):
        return self.__skill
    
    def SetSkill(self,increase): #Question c
        if increase>=10 and increase<=25:
            self.__skill=self.__skill+increase
            if self.__skill>=200:
                self.__skill=200
                return 0
            else:
                return 1
        else:
            return -1
        
CharacterArray=[None]*5 #question d
test=Character("Victory") #question e

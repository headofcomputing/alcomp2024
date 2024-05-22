import datetime
class Character():
    def __init__(self,charName,dateOfBirth,intel,speed):
        self.__CharacterName=charName #self.__CharacterName : STRING
        self.__DateOfBirth=dateOfBirth #self.__DateOfBirth : DATE
        self.__Intelligence=intel #self.__Intelligence : REAL
        self.__Speed=speed #self.__Speed : INTEGER

    def GetIntelligence(self):
        return self.__Intelligence
    
    def GetName(self):
        return self.__CharacterName
    
    def setIntelligence(self,pIntel):
        self.__Intelligence=pIntel

    def Learn(self):
        self.__Intelligence=self.__Intelligence*1.1
    
    import datetime
    def ReturnAge(self):
        return (2023-self.__DateOfBirth.year)

'''FirstCharacter=Character("Royal",datetime.date(2019,1,1),70,30)

FirstCharacter.Learn()
print("Name of character is",FirstCharacter.GetName())
print("age of this character is",FirstCharacter.ReturnAge())
print("intelligence of this character is",FirstCharacter.GetIntelligence())'''

class MagicCharacter(Character):
    def __init__(self,Element,CharName,DateBirth,Intel,Speed):
        super().__init__(CharName,DateBirth,Intel,Speed)
        self.__Element=Element #self.__Element : STRING

    def Learn(self):
        if self.__Element.lower()=="fire" or self.__Element.lower()=="water":
            super().setIntelligence(super().GetIntelligence()*1.2)
        elif self.__Element.lower()=="earth":
            super().setIntelligence(super().GetIntelligence()*1.3)
        else:
            super().Learn()

FirstMagic=MagicCharacter("fire","Light",datetime.date(2018,3,3),75,22)
FirstMagic.Learn()
print("Name of character is",FirstMagic.GetName())
print("age of this character is",FirstMagic.ReturnAge())
print("intelligence of this character is",FirstMagic.GetIntelligence())

class TreasureChest():
    def __init__(self,question,answer,points):
        #private self.__question : STRING
        #private self.__answer : STRING
        #private self.__points : integer
        self.__question=question 
        self.__answer=answer 
        self.__points=points 


    def getQuestion(self):
        return self.__question
    
    def checkAnswer(self,userAns):
        if userAns==self.__answer:
            return True
        else:
            return False
    
    def getPoints(self,attempts):
        if attempts==1:
            return self.__points
        elif attempts==2:
            return self.__points//2
        elif attempts==3 or attempts==4:
            return self.__points//4
        else:
            return 0

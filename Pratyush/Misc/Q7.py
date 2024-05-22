#KA we did in class

import random
class Animal():
    def __init__(self):
        self.__score=0
        self.__across=random.randint(0,39)
        self.__down=random.randint(0,39)

    def getAcross(self):
        return self.__across
    
    def setAcross(self,value):
        self.__across=value
        

class Desert():
    def __init__(self):
        self.__grid=[[None]*5]*5
        self.__animalList=[None]*5
        for i in range(0,5):
            self.__animalList[i]=Animal()
        #generateFood()
        self.__stepCounter=0
        self.__numberOfAnimals=5
    
    def generateChangeInCoordinate(coord):
        value=None
        if coord==0: #grid boundary value
            #zero or +1
            value=random.randint(0,1)
        elif coord==4: #grid boundary value
            #zero or -1
            value=random.randint(-1,0)
        else:
            #any
            value=random.randint(-1,1)
        return value

def generateChangeInCoordinate(coord):
    value=0
    if coord==0: #grid boundary value
        #zero or +1
        value=random.randint(0,1)
    elif coord==4: #grid boundary value
        #zero or -1
        value=random.randint(-1,0)
    else:
        #any
        value=random.randint(-1,1)
    return value
    
print(generateChangeInCoordinate(3))



yearList=[1992,1998,1960,1975,2000,1920,1965,1914,1914,2001,2003]

def bubbleSort(yearList):
    length=len(yearList)
    for i in range(0,length-1):
        for j in range(0,length-1-i):
            if yearList[j]>yearList[j+1]: #first bigger than second
                temp=yearList[j]
                yearList[j]=yearList[j+1]
                yearList[j+1]=temp
    return(yearList)

    
            

bob=Desert()
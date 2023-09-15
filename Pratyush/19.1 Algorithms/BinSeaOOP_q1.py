import random
def generateValues():
    array=[]
    for i in range(1000):
        array.append(random.randint(1,5000))
    array.sort()
    return array

class Binary():
    def __init__(self,array):
        self.__array=array

    def binarySearch(self,searchVal):
        found=False
        lowBound=0
        upBound=len(self.__array)-1
        index=(upBound+lowBound)//2
        while True:
            if self.__array[index]<searchVal:
                lowBound=index+1
            elif self.__array[index]>searchVal:
                upBound=index-1

            index=(upBound+lowBound)//2

            if self.__array[index]==searchVal:
                found=True
            
            if found==True or lowBound==upBound:
                break

        if found:
            return index
        else: 
            return -1

obj1=Binary(generateValues())
obj2=Binary(generateValues())
obj3=Binary(generateValues())

print(obj1.binarySearch(200))

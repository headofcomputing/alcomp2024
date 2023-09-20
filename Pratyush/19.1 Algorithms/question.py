import arrayGen
import InsertionSort
def binarySearch(array,searchVal):
        found=False
        lowBound=0
        upBound=len(array)-1
        index=(upBound+lowBound)//2
        while True:
            if array[index]<searchVal:
                lowBound=index+1
            elif array[index]>searchVal:
                upBound=index-1

            index=(upBound+lowBound)//2

            if array[index]==searchVal:
                found=True
            
            if found==True or lowBound==upBound:
                break

        if found:
            return index
        else: 
            return -1



class MyAlgorithm():
    def __init__(self):
        self.__array=arrayGen.generateValues(100,150)
    
    def linearSort(self):
        self.__array= InsertionSort.insertionSort(self.__array)
    
    def binarySearch(self,searchVal):
        return binarySearch(self.__array,searchVal)
        
objects=[None]*3
for i in range(0,3):
    objects[i]=MyAlgorithm()
    objects[i].linearSort()
    print(objects[i].binarySearch(21))

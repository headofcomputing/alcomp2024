import random
def generateValues(length,maxValue,minValue):
    array=[]
    for i in range(length):
        array.append(random.randint(minValue,maxValue))
    return array

myArray=generateValues(10,25,0)
print(myArray)

def insertionSort(array):
    length=len(array)
    currentPosition=1
    while currentPosition<length:
        key=array[currentPosition]
        this=currentPosition-1
        while key<array[this]:
            this -=1
        


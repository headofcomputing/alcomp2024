import random
def generateValues(length,maxValue,minValue):
    array=[]
    for i in range(length):
        array.append(random.randint(minValue,maxValue))
    return array
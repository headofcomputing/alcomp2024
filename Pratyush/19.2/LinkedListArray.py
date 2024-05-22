array=[[None for i in range(0,2)] for i in range(0,5)]
startPointer=None



#array[Row][Column]
#Row for data, column for pointer


def addData(data):
    global array,startPointer
    if startPointer==None:#empty
        array[0][0]=data
        array[0][1]=None
        startPointer=0
    elif startPointer==0:
        array[1][0]=data
        array[0][1]=1
    else: #Not empty
        nodePointer=array[0][1]
        while nodePointer!=None:
            prevPointer=nodePointer
            nodePointer=array[nodePointer][1]

        while array[nodePointer][0]!=None: #no free space
            nodePointer +=1 #go next
        else: #free space yes
            array[prevPointer][1]=nodePointer #add in
            array[nodePointer][0]=data
            array[nodePointer][1]=None
        

addData(1)
print(array)
addData(2)
print(array)
addData(3)
print(array)

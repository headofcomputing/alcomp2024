import arrayGen


class ArrayBehaviour():
    def __init__(self):
        self.__myArray=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        print(self.__myArray)

    def binarySearch(self,value): #has to be public becaise if it was __private the user could not call it
        found=False
        lowBound=0
        upBound=len(self.__myArray)-1
        mid=(upBound+lowBound)//2
        while found==False and lowBound!=upBound:
            

            if self.__myArray[mid]<value: #it is above

                lowBound=mid+1
            elif self.__myArray[mid]>value: #it is below

                upBound=mid-1
            mid=(upBound+lowBound)//2 #IMPORTANT for binary search this update mid value must be just before the check 
            #for edge cases which are checked below.
            
            if self.__myArray[mid]==value:

                found=True

        print(found)

class Stack():
    def __init__(self):
        self.__array=[None]*4
        self.__basePointer=0
        self.__topPointer=-1
        self.__stackFull=3
    
    def push(self,value):
        if self.__topPointer+1<=self.__stackFull:
            self.__topPointer=self.__topPointer+1
            self.__array[self.__topPointer]=value
        else:
            print('stack is full')
    
    def pop(self):
        if self.__topPointer==self.__basePointer-1:
            print('stack is empty')
        else:
            self.__topPointer=self.__topPointer-1
            self.__array[self.__topPointer+1]=None

    def pront(self):
        print(self.__array)

class Queue():
    def __init__(self):
        self.__array=[None]*5
        self.__front=0
        self.__rear=-1
        self.__currentLength=0
        self.__maxLength=5

    def enQueue(self,value):
        if self.__currentLength>=self.__maxLength:
            print('queue full')
        else:
            self.__rear +=1
            if self.__rear==self.__maxLength:
                self.__rear=0
            self.__array[self.__rear]=value
            self.__currentLength+=1
        print(self.__array)
    
    def deQueue(self):
        if self.__currentLength==0:
            print('queue empty')
        else:
            print('popping',self.__array[self.__front])
            self.__currentLength-=1
            self.__array[self.__front]=None
            print(self.__array)
            self.__front+=1
            if self.__front==5:
                self.__front=0

billy=Queue()
for i in range(0,6):
    billy.enQueue(i)

billy.deQueue()
billy.deQueue()
billy.deQueue()

billy.enQueue('sand')
billy.enQueue('wich')

billy.deQueue()
billy.deQueue()
billy.deQueue()

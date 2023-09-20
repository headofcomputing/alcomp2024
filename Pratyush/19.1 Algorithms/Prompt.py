import arrayGen
import InsertionSort

def linearSearch(array,searchVal):
    comparisons=0
    found=False
    for i in range(0,len(array)):
        comparisons=comparisons+1
        if array[i]==searchVal:  
            found=True
            break
    if found:
        print("found in Linear")
    else:
        print('not found in linear')
    
    bubbleSort(array,comparisons,searchVal)



def bubbleSort(array,totalComparisons,targetValue):
    sorted=False

    maxBound=len(array)-1
    counter=0
    while sorted==False and counter<maxBound:
        swaps=False
        for i in range(0,maxBound-counter):
            if array[i]<array[i+1]:
                swaps=True
                temp=array[i]
                array[i]=array[i+1]
                array[i+1]=temp

        if swaps==False:
            sorted==True
        counter=counter+1
    print("\nbubble sorted list")
    print(array)

    binarySearchX(array,targetValue,totalComparisons)
    



def binarySearchX(array,searchval,LinearComparisons):
    upperBound=len(array)-1
    lowerBound=0
    found=False
    index=(upperBound+lowerBound)//2
    comparisons=0


    while True:
        index=(upperBound+lowerBound)//2
        if searchval>array[index]:
            lowerBound=index+1
        elif searchval<array[index]:
            upperBound=index-1

        

        elif searchval==array[index]: #check
            found=True
        
        comparisons=comparisons+1

        if found==True or lowerBound==upperBound:
            break
    
    if found:
        print("found, using Binary Search")
    else:
        print("not found, using Binary Search")

    print('\nbinary search took',comparisons,'comparisons')
    print('difference in comparisons:',LinearComparisons-comparisons)
    print('running insertion sort')
    print(InsertionSort.insertionSort(array))


myList=arrayGen.generateValues(15,50,12)
print('\n')
print(myList)



linearSearch(myList,20)





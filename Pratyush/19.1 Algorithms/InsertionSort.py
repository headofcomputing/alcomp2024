import arrayGen



def insertionSort(array):
    lowerBound=0
    upperBound=len(array)
    for i in range(lowerBound+1,upperBound):
        key=array[i]
        j=i-1
        while j>=lowerBound and array[j]>key:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=key
    
    return(array)


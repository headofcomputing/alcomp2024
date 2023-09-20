

def bubbleSort(array):
    sorted=False

    maxBound=len(array)-1
    counter=0
    while sorted==False and counter<maxBound:
        swaps=False
        for i in range(0,maxBound-counter):
            if array[i]>array[i+1]:
                swaps=True
                temp=array[i]
                array[i]=array[i+1]
                array[i+1]=temp

        if swaps==False:
            sorted==True
        counter=counter+1
  
    return array




            

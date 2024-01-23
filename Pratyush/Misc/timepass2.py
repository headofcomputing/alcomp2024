dataArray=[4,7,9,1,2,10,12,8,13,19,0]

def insertionSort():
    global dataArray
    length=len(dataArray)
    for i in range(1,length):
        key=dataArray[i]
        j=i-1
        while key>dataArray[j] and j>=0:
            dataArray[j+1]=dataArray[j]
            j=j-1
            print(dataArray)
        dataArray[j+1]=key
        print('')
    print(dataArray)

insertionSort()

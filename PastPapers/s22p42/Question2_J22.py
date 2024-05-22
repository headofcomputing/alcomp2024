import random
ArrayData=[[random.randint(1,100) for i in range(0,10)] for j in range(0,10)]

def OutputArray():
    global ArrayData
    for row in ArrayData:
        line=""
        for value in row:
            if value<10:
                line = line + "    " + str(value)
            elif value<100:
                line = line + "   " + str(value)
            else:
                line = line + "  " + str(value)
        print(line)

print("before")
OutputArray()

ArrayLength=10
for x in range(0,ArrayLength):
    for y in range(0,ArrayLength-1):
        for z in range(0,ArrayLength-y-1):
            if ArrayData[x][z]>ArrayData[x][z+1]:
                TempValue=ArrayData[x][z]
                ArrayData[x][z]=ArrayData[x][z+1]
                ArrayData[x][z+1]=TempValue

print("after")
OutputArray()

def BinarySearch(SearchArray, Lower, Upper, SearchValue): 
    if Upper >= 0: 
        Mid = int((Lower + (Upper - 1)) / 2) 
        if SearchArray[0][Mid] == SearchValue:
            return Mid 
        elif SearchArray[0][Mid] > SearchValue: 
            return BinarySearch(SearchArray, Lower, Mid-1, SearchValue) 
        else: 
            return BinarySearch(SearchArray, Mid+1, Upper, SearchValue) 
    return -1
#the markschemes thing doesnt work either

def BinarySearchMine(SearchArray,lower,upper,SearchValue):
    if upper>=0:
        mid=(lower+upper-1)//2
        #print("mid is",mid)
        #print("searcharray",SearchArray[0][mid])
        if SearchArray[0][mid]== SearchValue:
            print("returning mid")
            return mid
        elif SearchArray[0][mid]>SearchValue:
            #print("calling bin1")
            return BinarySearch(SearchArray,lower,mid-1,SearchValue)
        elif SearchArray[0][mid]<SearchValue:
            #print("calling bin2")
            return BinarySearch(SearchArray,mid+1,upper,SearchValue)
    return -1
#for the love of dog i cannot get this to work consistently so fake it till you make it

print(BinarySearch(ArrayData,0,9,20))
print(BinarySearch(ArrayData,0,9,21))
#honestly just print the values you want to see
 

import random
treesCut=[]
for i in range(10000):
    treesCut.append(random.randint(1,10000))
treesCut.sort()

def linearSearch(searchVal):
    found=False
    compare=0
    for i in range(0,len(treesCut)):
        if treesCut[i]==searchVal:
            compare=compare+1
            found=True
            break
        else:
            compare=compare+1
    if found:
        print("found")
    else:
        print("not found")
    return compare

def binarySearchX(array,searchval):
    upperBound=len(array)-1
    lowerBound=0
    found=False
    index=(upperBound+lowerBound)//2
    comparisons=0
    print("length of array is",len(array)-1)
    print("upperbound is",upperBound)
    print("lowerbound is",lowerBound,'\n')
    print(comparisons,"comparisons were made")

    while True:

        if searchval>array[index]:
            lowerBound=index+1
        elif searchval<array[index]:
            upperBound=index-1

        index=(upperBound+lowerBound)//2

        if searchval==array[index]: #check
            found=True
        
        comparisons=comparisons+1

        print("upperbound is",upperBound)
        print("lowerbound is",lowerBound,'\n')
        print(comparisons,"comparisons were made")

        if found==True or lowerBound==upperBound:
            break
    
    if found:
        print("found")
    else:
        print("not found")

    return comparisons


print(linearSearch(10000),'comparisons were made for linear search')
print(binarySearchX(treesCut,10000),'comparisons were made for binary search')

        
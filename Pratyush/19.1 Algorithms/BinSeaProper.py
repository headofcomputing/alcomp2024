arrayNums=[2,3,3,4,9,12,15,17,21,25,36,42,47,51,62,73,74,89,99,100,101,102,107,120,150,180]

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


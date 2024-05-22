import itertools

def SumLargestProduct(TargetNum):
    oneTarget=[]
    for i in range(2,TargetNum+1):
        oneTarget.append(i)
    #print (oneTarget)

    triangleNum=1
    counter=2
    while triangleNum+counter<TargetNum:
        triangleNum+=counter
        counter+=1
    
    #print(counter,triangleNum)
    
    superHighestProd=0

    for i in range(2,counter):
        combinations = list(itertools.combinations(oneTarget,i))
        Array=[]
        highestProd=1
        for elemement in combinations:
            total=0
            for unit in elemement:
                total=total+unit
            if total==TargetNum:
                Array.append(elemement)

        for element in Array:
            product=1
            highestProd=1
            for unit in element:
                product=product*unit
            if product>highestProd:
                highestProd=product

            #print(highestProd, element)

        if highestProd>superHighestProd:
            #print("current greater than highest")
            superHighestProd=highestProd
            highestArray=element
    #print("\n",superHighestProd,highestArray, "makes highest product and sums to", TargetNum)
    return (superHighestProd,highestArray)
        
def SixNumbers(): 
    oneSix=[1,2,3,4,5,6]
    permutations = list(itertools.permutations(oneSix, 6))

    for element in permutations:
        num1=int(str(element[0])+str(element[1]))
        num3=int(str(element[3])+str(element[4])+str(element[5]))
        if num1 * element[2] ==num3:
            print(element)

for i in range(5,31):
    print(i,SumLargestProduct(i))
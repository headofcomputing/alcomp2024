#hello guys welcome to my code today we are learnging binary seachrthch!!121!1!!
#this is will be the funy i think
arrayNums=[2,3,3,4,9,12,15,17,21,25,36,42,47,51,62,73,74,89,99]

#find midpoint integer value of lower bound and upper bound
#compare if the midpoint is equal to search
'''if search less than midpoint shift upper bound to midpoint
if search more than midpoint shift lower bound to midpoint
repeat process of midpoint, shifting the bounds
until value found'''

def binarySearch(array,searchval):
    found=False
    upperBound=len(array)
    lowerBound=0
    comparisons=0
    midpoint=(upperBound+lowerBound)//2

    while found==False :
        midpoint=(upperBound+lowerBound)//2
        print("midpoint is",midpoint)
        
        if array[midpoint]>searchval:
            upperBound=midpoint-1
            comparisons=comparisons+1

        elif array[midpoint]<searchval:
            lowerBound=midpoint+1
            comparisons=comparisons+1
            
        else: 
            found=True
            
        if  upperBound==lowerBound:
            break
        print("upperbound is",upperBound)
        print("lowerbound is",lowerBound,'\n')
        print(comparisons,"comparisons were made")

    

    return found

        


searchResult=binarySearch(arrayNums,2)
print(searchResult)

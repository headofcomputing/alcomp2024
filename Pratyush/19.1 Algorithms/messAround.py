def linearSearch(array,searchVal):
    found=False
    for i in range (0,len(array)):
        if array[i]==searchVal:
            found=True
            break
    if found:
        print("found")
    else:
        print("nuhj uh")


def binSearch(array,searchVal):
    lb=0
    ub=len(array)-1

    while lb<=ub:
        mid=(lb+ub)//2

        if array[mid]<searchVal:
            lb=mid+1
        elif array[mid]>searchVal:
            ub=mid-1
        else:
            print (mid)
            break #found the value
    print (-1)

binSearch([1,2,3,4,5,6,7,8,9,10],5)

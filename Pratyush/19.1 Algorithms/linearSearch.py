import random
import math

numList=[None]*50
for i in range(0,50):
    numList[i]=random.randint(1,100)

def isPrime(number):
    if number<=1:
        return False
    else:
        num2=int(math.sqrt(number))+1
        flag=True
        for i in range(2,num2):
            if number%i==0:
                flag=False
        return flag


def countIt(array):
    oddList=[]
    primeList=[]
    evenList=[]
    countPrimes=0
    countOdd=0
    countEven=0
    for i in range(0,50):
        if array[i]%2==0:
            countEven=countEven+1
            evenList.append(array[i])
        else:
            countOdd=countOdd+1
            oddList.append(array[i])
        if isPrime(array[i]):
            countPrimes=countPrimes+1
            primeList.append(array[i])

    print("there are",countOdd,"odd Numbers")
    print("there are",countEven,"even Numbers")
    print("there are",countPrimes,"prime Numbers")
    
    return oddList, evenList, primeList

print(countIt(numList))



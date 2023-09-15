import random
import math


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


class Linear:
    def __init__(self):
        numList=[None]*50
        for i in range(0,50):
            numList[i]=random.randint(1,100)
        self.__toSort=numList
        self.__oddList=[]
        self.__evenList=[]
        self.__primeList=[]

    def linearSearch(self):
            countPrimes=0
            countOdd=0
            countEven=0
            for i in range(0,50):
                if self.__toSort[i]%2==0:
                    countEven=countEven+1
                    self.__evenList.append(self.__toSort[i])
                else:
                    countOdd=countOdd+1
                    self.__oddList.append(self.__toSort[i])
                if isPrime(self.__toSort[i]):
                    countPrimes=countPrimes+1
                    self.__primeList.append(self.__toSort[i])

            print("there are",countOdd,"odd Numbers")
            print("there are",countEven,"even Numbers")
            print("there are",countPrimes,"prime Numbers")
            

    def getOddList(self):
        return self.__oddList
    
    def getEvenList(self):
        return self.__evenList
    
    def getPrimeList(self):
        return self.__primeList
    
#create 3 object instances
object1=Linear()
object1.linearSearch()
print("even nums",object1.getEvenList(),"odd nums",object1.getOddList(),"prime nums",object1.getPrimeList())
object2=Linear()
object3=Linear()



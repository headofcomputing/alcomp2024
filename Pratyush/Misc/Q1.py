def Unknown(X,Y):
    if X<Y:
        print(X+Y)
        return (Unknown(X+1,Y)*2)
    else:
        if X==Y:
            return 1
        else:
            print(X+Y)
            return(Unknown(X-1,Y)//2)
        


def IterativeUnknown(X,Y):
    returnValue=1
    while True:
        if X==Y:
            return returnValue
        elif X<Y:
            print(X+Y)
            returnValue=returnValue*2
            X=X+1
        else:
            print(X+Y)
            returnValue=returnValue//2
            X=X-1


def functionCall(X,Y):
    print('function Unknown has been called')
    print("the two parameters X and Y are",X,'and',Y,'respectively')
    returnValue=Unknown(X,Y)
    print('return value is',returnValue,'\n')


def functionCallIterative(X,Y):
    print('function IterativeUnknown has been called')
    print("the two parameters X and Y are",X,'and',Y,'respectively')
    returnValue=IterativeUnknown(X,Y)
    print('return value is',returnValue,'\n')

functionCall(10,15)
functionCall(10,10)
functionCall(15,10)

functionCallIterative(10,15)
functionCallIterative(10,10)
functionCallIterative(15,10)


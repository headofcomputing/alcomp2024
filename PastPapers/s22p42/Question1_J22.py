#global, in main program
StackData=[None]*10     #array of INTEGER
StackPointer=0

def OutputAll():
    global StackData, StackPointer
    print(StackData, "are values of StackData") #markscheme suggest printing them one by one
    print("StackPointer value is",StackPointer)

def Push(value): #value : INTEGER
    global StackData, StackPointer
    if StackPointer>9:
        return False
    else:
        StackData[StackPointer]=value
        StackPointer +=1
        return True

#in main program
for i in range(0,11):
    userValue=int(input("please enter an integer: "))
    if Push(userValue)==True:
        print("number pushed successfully")
    else:
        print("Stack is full, could not push number")
OutputAll()

def Pop():
    global StackData, StackPointer
    if StackPointer==0:
        return -1
    else:
        StackPointer-=1
        return StackData[StackPointer]
    
Pop()
Pop()
OutputAll()
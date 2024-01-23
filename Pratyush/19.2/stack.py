global stack
stack=[None]*5
global topPointer
topPointer=-1
global basePointer
basePointer=0
global stackFull
stackFull=4

def push(value):
    global topPointer
    global stackFull
    global stack
    
    if topPointer<stackFull:
        topPointer=topPointer+1
        stack[topPointer]=value
        print('successfully pushed value')
    else:
        print('error: stack is full')
    

push(1)
push(3)
push(5)
push(5)
print(stack)
push(5)
push(5)
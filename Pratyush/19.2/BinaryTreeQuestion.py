#W21 p41

ArrayNodes=[[None for i in range(0,3)]for i in range(0,20)] #DECLARE ArrayNodes : Array[0:2,0:19] OF INTEGER
RootPointer=-1 #DECLARE RootPointer : Integer
FreeNode=0 #DECLARE FreeNode : Integer

def AddNode():
    global ArrayNodes,RootPointer,FreeNode #MS says taking global is fine
    NodeData=int(input("enter the data "))
    if FreeNode<=19:
        ArrayNodes[FreeNode][0]=-1
        ArrayNodes[FreeNode][1]=NodeData
        ArrayNodes[FreeNode][2]=-1
        if RootPointer==-1:
            RootPointer=0
        else:
            Placed=False
            CurrentNode=RootPointer
            while Placed==False:
                if NodeData<ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0]==-1:
                        ArrayNodes[CurrentNode][0]=FreeNode
                        Placed=True
                    else:
                        CurrentNode=ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2]=FreeNode
                        Placed=True
                    else:
                        CurrentNode=ArrayNodes[CurrentNode][2]
        FreeNode=FreeNode+1
    else:
        print("Tree is Full")


def PrintAll():
    global ArrayNodes
    for i in range(0,20):
        print(ArrayNodes[i][0]," ",ArrayNodes[i][1]," ",ArrayNodes[i][2])

for i in range(0,10):
    AddNode()


PrintAll()

def InOrder(currentNode):
    global ArrayNodes
    #print('currentNode',currentNode)
    leftPointer=ArrayNodes[currentNode][0]
    #print(leftPointer)
    rightPointer=ArrayNodes[currentNode][2]
    #print(rightPointer)

    if currentNode==-1: #Null node
        pass
    else:
        if leftPointer!=-1: #LP not null means node on Left Side
            #print("going Down Left side")
            InOrder(leftPointer)


        print(ArrayNodes[currentNode][1]) #print its own value
        
            
        #Now for Right Side
        if rightPointer!=-1:    #RP not Null, value on right                        
            #print("going down Right Side")
            InOrder(rightPointer)
        else: #RP is NULL
            pass #Nothing else on right


        


InOrder(0)     



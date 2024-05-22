import simple_colors
'''class ListElement():
    def __init__(self,country,pointer):
        self.Country=country
        self.Poineter=pointer

    
CountryList=[None]*15 #ARRAY of type ListElement
'''
def boardGame():
    board=[['E' for i in range(0,8)] for j in range(0,8)]

    for i in range(0,8):
        board[0][i]='B'
        board[1][i]='B'
        board[7][i]='W'
        board[6][i]='W'

    board[4][4]='W'
    board[4][7]='W'
    board[4][3]='B'

    for line in board:
        for piece in line:
            if piece=="W":
                print(simple_colors.blue(piece),end="")
            elif piece=="B":
                print(simple_colors.red(piece),end="")
            else:
                print(piece,end="")
        print("")

    def ValidMoves(PieceColour,xCurrent,yCurrent):
        board
        #Left first
        print("Moving LEFT")
        xTracking=xCurrent-1
        while True:
            if xTracking<0 or board[yCurrent][xTracking]==PieceColour:
                break
            elif board[yCurrent][xTracking]=='E':
                print(xTracking,yCurrent)
            else: #opponent piece
                print(xTracking,yCurrent, "REMOVE piece")
                break
            xTracking-=1

        #Right now
        print("Moving RIGHT")
        xTracking=xCurrent+1
        while True:
            if xTracking>7 or board[yCurrent][xTracking]==PieceColour:
                break
            elif board[yCurrent][xTracking]=='E':
                print(xTracking,yCurrent)
            else: #opponent piece
                print(xTracking,yCurrent, "REMOVE piece")
                break
            xTracking+=1



    ValidMoves('W',4,4)

class Node():
    def __init__(self,data,pointer):
        self.data=data
        self.pointer=pointer


class LinkedList():
    def __init__(self):
        self.__headpointer=None
        self.__nodeArray=[None]*7
        self.__freeListPointer=0
        for i in range(0,6):
            self.__nodeArray[i]=Node("",i+1)
        self.__nodeArray[6]=Node("",None)
    
    def printNodeArray(self):
        for item in self.__nodeArray:
            print(item.data, "", item.pointer)

    def FindInsertionPoint(self,NewData):
        if self.__headpointer==None:
            PreviousPointer=None
            NextPointer=self.__freeListPointer
        else:
            CurrentPointer=self.__headpointer
            while self.__nodeArray[CurrentPointer].pointer!=None:
                PreviousPointer=CurrentPointer
                CurrentPointer=self.__nodeArray[CurrentPointer].pointer
                NextPointer=CurrentPointer
        return PreviousPointer,NextPointer
    
    def InsertData(self,NewString):
        NewNodePointer=self.__freeListPointer
        self.__nodeArray[NewNodePointer].data=NewString
        self.__freeListPointer=self.__nodeArray[NewNodePointer].pointer
        if self.__headpointer==None:
            self.__headpointer==NewNodePointer
            self.__nodeArray[NewNodePointer].pointer=None
        else:
            values=self.FindInsertionPoint()
            self.__nodeArray[values[0]].pointer=NewNodePointer
            self.__nodeArray[NewNodePointer].pointer=values[1]


                
            
boardGame()

myList=LinkedList()

#print(myList.FindInsertionPoint("apple"))
myList.InsertData("apple")
myList.InsertData("banana")

myList.printNodeArray()


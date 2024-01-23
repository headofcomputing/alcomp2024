class Node():
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class SLinkedList():
    def __init__(self):
        self.headval=None

    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval

    def Inbetween(self,middle_node,newdata):
      if middle_node is None:
         print("The mentioned node is absent")
         return

      NewNode = Node(newdata)
      NewNode.nextval = middle_node.nextval
      middle_node.nextval = NewNode        

    def InBegin(self,newData):
        newNode=Node(newData)
        newNode.nextval=self.headval
        self.headval=newNode

    def search(self,searchVal):
        currentNode=self.headval
        while currentNode is not None:
            if searchVal==currentNode.dataval:
                print("found")
                return True
            currentNode=currentNode.nextval
        print("Not Found")
        return False
    
    def addNode(self,node):
        printval=self.headval
        while printval.nextval is not None:
            printval=printval.nextval
        printval.nextval=node
        

    def deleteNode(self,value):
        if self.headval==None: #linked list empty
            return False
        else:
            currentPointer=self.headval
            if currentPointer.dataval==value: #if its first value
                return True
            else: #not first value
                previousPointer=currentPointer
                while currentPointer!=None and currentPointer.dataval!=value:
                    previousPointer=currentPointer
                    currentpointer=currentPointer.nextval
                if currentPointer==None: #at end of list
                    if currentPointer.dataval==value: #last value is search value
                        previousPointer.nextval=None
                        return True
                    else:
                        return False
                else:
                    if currentPointer.dataval==value:

                


list1=SLinkedList()
list1.headval=Node("A")
list1.addNode(Node('B'))
list1.addNode(Node('E'))
list1.addNode(Node('C'))
list1.addNode(Node('D'))
list1.listprint()




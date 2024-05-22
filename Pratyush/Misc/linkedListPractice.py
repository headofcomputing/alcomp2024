class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList():
    def __init__(self):
        self.head=None

    def append(self,data):
        if self.head==None:
            self.head=Node(data)
        else: #traverse link list until end
            thisNode=self.head
            while thisNode.next!=None:
                thisNode=thisNode.next
            thisNode.next=Node(data)
    
    def printList(self):
        if self.head==None:
            print("list empty")
        else:
            thisNode=self.head
            while thisNode!=None:
                print(thisNode.data)
                thisNode=thisNode.next

    def prepend(self,data):
        temp=self.head
        self.head=Node(data)
        self.head.next=temp

    def intsertAfterNode(self,position,data):
        try:
            thisNode=self.head
            while thisNode.data!=position:
                thisNode=thisNode.next
            temp=thisNode.next
            thisNode.next=Node(data)
            thisNode.next.next=temp
        except:
            print("error: could not find the position you wanted to place node in")

myLinkedList=LinkedList()

myLinkedList.append("apple")
myLinkedList.append("banana")
myLinkedList.append("carrot")
myLinkedList.prepend("wait")
myLinkedList.intsertAfterNode("wait","ok continue")
myLinkedList.printList()
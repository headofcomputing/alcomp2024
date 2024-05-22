class Node():
    def __init__(self,data):
        self.value=data
        self.right=None
        self.left=None

class BinaryTree():
    def __init__(self):
        self.root=None
    
    def insertValue(self,data):
        if self.root==None:
            self.root=Node(data)
        else:
            currentNode=self.root

            while True:
                if currentNode.value>data: 
                    if currentNode.left==None:
                        currentNode.left=Node(data)
                        return
                    else:
                        currentNode=currentNode.left

                elif currentNode.value<data:
                    if currentNode.right==None:
                        currentNode.right=Node(data)
                        return
                    else:
                        currentNode=currentNode.right

    def FakeprintValues(self):
        def Rec (val):
            if val==None:
                pass
            else:
                print(Rec(val.left))
                print(val.value)
                print(Rec(val.right))
        Rec(self.root)
    
    def RealPrintValues(self):
        pass


                

test=BinaryTree()
test.insertValue(5)
test.insertValue(4)
test.printValues()
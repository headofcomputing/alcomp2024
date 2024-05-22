class Node():
    def __init__(self,value):
        self.left=None
        self.right=None
        self.val=value

class BinaryTree():
    def __init__(self):
        self.root=None

    def add_node(self,value):
        new_node=Node(value)
        if self.root is None:
            self.root = new_node
        return

        current=self.root
    

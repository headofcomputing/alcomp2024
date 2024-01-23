class Stack():
    def __init__(self,size):
        self.stack=[None]*size
        self.topPointer=-1
        self.basePointer=0
        self.stackFull=size-1

    def push(self,value):
        if self.topPointer<self.stackFull:
            self.topPointer=self.topPointer+1
            self.stack[self.topPointer]=value
            print('successfully pushed value')
        else:
            print('error: stack is full')

    def pop(self):
        if self.topPointer==self.basePointer-1:
            print('stack is empty: cannot pop')
        else:
            item=self.stack[self.topPointer]
            self.topPointer=self.topPointer-1
            return item
        
    def show(self):
        print(self.stack)
    

myStack=Stack(5)
myStack.push(1)
myStack.show()
print(myStack.pop())
myStack.pop()

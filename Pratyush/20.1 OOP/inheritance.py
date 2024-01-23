class A:
    def __init__(self):
        print('A was used to initialise')
        pass
    def printData(self):
        print("A method")

class B(A):
    def __init__(self):
        print('B was used to initialise')
        pass

    def turtle(self):
        print('b was used for this method')

obj=B()
obj.printData()

class b():
    def doSomething(self):
        print('hi')

class a():
    def __init__(self,value):
        self.__value=value

    def thing(self):
        self.__value.doSomething()



value=b()

apple=a(value)

apple.thing()




            

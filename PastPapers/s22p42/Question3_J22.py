class Card():
    def __init__(self,colour,number):
        self.__number=number #self.__number : INTEGER
        self.__colour=colour #self.__colour : STRING

    def GetNumber(self):
        return self.__number
    
    def GetColour(self):
        return self.__colour
    
CardArray=[None]*30 #of type Card
try:
    Myfile=open("PastPapers\s22p42\CardValues.txt",'r')
    for i in range(0,30):
        Number1=int(Myfile.readline().strip())
        Color1=Myfile.readline().strip()
        CardArray[i]=Card(Color1,Number1)
    Myfile.close()
except IOError:
    print("error: file not found")

numbersChosen=[]
def ChooseCard(index):
    global CardArray,numbersChosen
    Cont=False
    while Cont==False:
        if index>30 or index<1:
            index=int(input("please enter a valid index between 1 and 30"))
        for thing in numbersChosen:
            if thing==index:
                print("cant choose that") #already chosen
                index=int(input("Please enter different valid number between 1 and 30"))
    numbersChosen.append(index)
    return index-1

ChooseCard(-1)
print(numbersChosen)
ChooseCard(-1)
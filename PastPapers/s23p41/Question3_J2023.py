Animal=[None]*20 #ARRAY of 20 STRING elements
Colour=[None]*10 #ARRAY of 10 STRING elements
AnimalTopPointer=0 #INTEGER
ColourTopPointer=0 #INTEGER

def PushAnimal(DataToPush):
    global AnimalTopPointer,Animal
    if AnimalTopPointer==20:
        return False
    else:
        Animal[AnimalTopPointer]=DataToPush
        AnimalTopPointer+=1
        return True
    
def PopAnimal():
    global Animal,AnimalTopPointer
    if AnimalTopPointer==0:
        return ""
    else:
        ReturnData=Animal[AnimalTopPointer-1]
        AnimalTopPointer -=1
        return ReturnData
    
    
def PushColour(DataToPush):
    global Colour,ColourTopPointer
    if ColourTopPointer==10:
        return False
    else:
        Colour[ColourTopPointer]=DataToPush
        ColourTopPointer +=1
        return True

def PopColour():
    global Colour,ColourTopPointer
    if ColourTopPointer==0:
        return ""
    else:
        ReturnData=Colour[ColourTopPointer-1]
        ColourTopPointer -=1
        return ReturnData
    

def ReadData():
    try:
        f1=open("AnimalData.txt",'r')
        for line in f1:
            PushAnimal(line.strip())
        f1.close()
    except IOError:
        print("Error: Animal Data File not found")
    
    try:
        f2=open("ColourData.txt",'r')
        for line in f2:
            PushColour(line.strip())
        f1.close()
    except IOError:
        print("Error: Colour Data file not found")

def OutputItem():
    myColour=PopColour()
    myAnimal=PopAnimal()
    if myColour=="": #nothing in Colour
        PushAnimal(myAnimal)
        print("No colour")
    elif myAnimal=="": #nothing in animal
        PushColour(myColour)
        print("No animal")
    else:
        print(myColour,myAnimal)


ReadData()
for i in range(0,4):
    OutputItem()



#9618 41 m j 21
#2a

arrayData=[10,5,6,7,1,12,13,15,21,8]

def bubbleSort():
    global arrayData
    for x in range(0,9):
        for y in range(0,9-x):
            if arrayData[y]<arrayData[y+1]:
                temp=arrayData[y]
                arrayData[y]=arrayData[y+1]
                arrayData[y+1]=temp
    print(arrayData)

bubbleSort()

def linearSearch(value):
    global arrayData
    for element in arrayData:
        if element==value:
            return True
    return False

userInput=int(input("please enter an integer value"))
found=linearSearch(userInput)
if userInput==True:
    print("the value was found in the array")
else:
    print("the value was not found in the array")


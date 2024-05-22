DataArray=[] #type ARRAY of INTEGER of 25 elements

f1=open("Data.txt",'r')
for line in f1:
    DataArray.append(int(line.strip()))



def PrintArray(array):
    output=""
    for item in array:
        output=output+str(item)+ " "
    print(output)



def LinearSearch(array,searchVal):
    counter=0
    for element in array:
        if (element)==(searchVal):
            counter=counter+1
    return counter

num=int(input("please enter a number from 0 to 100 inclusive "))
while num<=0 or num>=100:
    num=int(input("wrong input. please only enter a number from 0 to 100 inclusive "))
print("The number",num,"is found",LinearSearch(DataArray,num),"times")
#PrintArray(DataArray)
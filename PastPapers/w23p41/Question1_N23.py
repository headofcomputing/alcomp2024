#Question 1
def IterativeVowel(value): #value: STRING
    Total=0
    LengthString=len(value)
    for x in range (0,LengthString):
        FirstCharacter=value[0]
        if FirstCharacter=='a' or FirstCharacter=='e' or FirstCharacter=='i' or FirstCharacter=='o' or FirstCharacter=='u':
            Total=Total+1
        value=value[1:(len(value))]
    return Total

#print(IterativeVowel("house"))

def RecursiveVowels(value):
    if value=="":#base case
        return 0
    else:
        FirstCharacter=value[0]
        if FirstCharacter=='a' or FirstCharacter=='e' or FirstCharacter=='i' or FirstCharacter=='o' or FirstCharacter=='u':
            return 1+RecursiveVowels(value[1:(len(value))])
        else:
            return 0+RecursiveVowels(value[1:(len(value))])

    #recall

print(RecursiveVowels("imagine"))
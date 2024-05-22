StackVowel=[None]*100 #StackVowel : ARRAY of 100 CHAR
StackConsonant=[None]*100 #StackConsonant : ARRAY of 100 CHAR

VowelTop=0 #VowelTop : INTEGER
ConsonantTop=0 #ConsonantTop : INTEGER

def PushData(letter):
    global VowelTop,ConsonantTop,StackVowel,StackConsonant
    if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
        #vowel
        if VowelTop==100: 
            print("vowel stack is full, could not push")
        else:
            StackVowel[VowelTop]=letter
            VowelTop+=1


    else:
        #consonant
        if ConsonantTop==100:
            print("consonant stack is full, could not push")
        else:
            StackConsonant[ConsonantTop]=letter
            ConsonantTop+=1
    
def ReadData():
    try:
        f1=open("StackData.txt",'r')
        while True:
            line=(f1.readline()).strip()
            if line=="":
                break
            else:
                PushData(line)
        f1.close()

    except IOError:
        print("file not found / file does not exist")

def PopVowel():
    global VowelTop,StackVowel
    if VowelTop==0:
        return("No data")
    else:
        VowelTop-=1
        return StackVowel[VowelTop]
    
def PopConsonant():
    global ConsonantTop,StackConsonant
    if ConsonantTop==0:
        return("No data")
    else:
        ConsonantTop-=1
        return StackConsonant[ConsonantTop]

#main program, Q d(i)
ReadData()

store=""

for i in range(0,5):
    letter=str(input("please enter a vowel or consonant of your choice "))

    if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
        temp=PopVowel()
        if temp=="No data":
            print("Vowel stack is empty.")
        store=store+temp
    else:
        temp=PopConsonant()
        if temp=="No data":
            print("Consonant stack is empty.")
        store=store+temp

print(store)

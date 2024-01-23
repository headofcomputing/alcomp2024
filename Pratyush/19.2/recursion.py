def factorial(number):
    if number==0:
        answer=1
    else:
        answer=number*factorial(number-1)
        print('doing factorial',number-1)
    return answer

def fibonnacci(number):
    if number==1:
        answer=0
    elif number==2:
        answer=1
    else:
        answer=fibonnacci(number-1)+fibonnacci(number-2)
    return answer

def sumNumber(number):
    if number==0:
        answer=0
    else:
        answer=number+sumNumber(number-1)
    return answer

def reverse_string(s):
       if len(s)==1:
           return s
       else:
           lastLetter=reverse_string(s[len(s)-1])
           restOfWord=s[0:len(s)-1]
           return lastLetter+reverse_string(restOfWord)

nestedArray=[1,2,3,4,[5,6,7],[8,9,[10,11,12,13,14],15,16],17,18,[19,20]]


def nestedSum(array):
    sum=0
    for i in range(0,len(array)):       #go through the array
        if isinstance(array[i],int):    #is integer
            sum=sum+array[i]            #add to sum
        else:                           #is not integer (hence its a list)
            sum=sum+nestedSum(array[i]) #find sum of that list (recursive call)
    return sum

def power(base, exponent):
    if exponent==0:
        return 1
    else:
        return base*power(base,exponent-1)

def is_palindrome(s):
       reversedString=reverse_string(s)
       if reversedString==s:
           return True
       else:
           return False

def flatten_list(lst):
    flatList=[]

    for i in range(0,len(lst)):       
        if isinstance(lst[i],list):    #if is list
            tempList=lst[i]
            tempList=flatten_list(tempList) #flatten it
            for i in range(0,len(tempList)):  
                  flatList.append(tempList[i])   #individually append values     

        else:       #its integer                    
            flatList.append(lst[i])   #append
            
    return flatList

def permutations(lst):
    if len(lst) == 0: #base case; list empty
        return [[]]

    rest_permutations = permutations(lst[1:]) #find permutations for the rest of it

    result = [] #intitialise empty list of results
    first = lst[0] 
    for perm in rest_permutations:
        for i in range(len(perm) + 1):
            result.append(perm[:i] + [first] + perm[i:])
    return result

        



print(permutations([1,2,3]))











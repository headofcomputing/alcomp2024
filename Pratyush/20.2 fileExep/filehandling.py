

def user_registration():  
    f1=open("user_into.txt",'w')
    for i in range(0,5):
        text=input('please enter name of the student ')
        f1.write(text+'\n')
    f1.close()

def display_users():
    f1=open("user_into.txt",'r')
    for i in range(0,5):
        print(f1.readline().strip())
    f1.close()

def check_users(user):
    f1=open("user_into.txt",'r')
    for i in range(0,5):
        a=f1.readline().strip()
        if user==a:
            return 1
    f1.close()
    return 0

def user_age():
    f2=open('users_age.txt','w')
    for i in range(0,5):
        text=input('please enter age of the student ')
        f2.write(text+'\n')
    f2.close()



def combine_display():
    f1=open('user_into.txt','r')
    f2=open('users_age.txt','r')
    value=input('please enter either the students age or the students age ')
    counter=0
    flag=False
    while counter<5 and flag==False:
        x=f1.readline().strip()
        y=f2.readline().strip()
        if x==value or y==value:
            flag=True
        counter=counter+1
    print(x,' ',y)

combine_display()
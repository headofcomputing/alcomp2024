
Queue=[] #Queue: ARRAY of STRING
HeadPointer=-1 #INTEGER first element in queue
TailPointer=0 #INTEGER next available space in queue

def Enqueue(string):
    global Queue, HeadPointer,TailPointer
    if TailPointer>49:
        print("queue is full")
    else:
        Queue.append(string)
        TailPointer=TailPointer+1
        HeadPointer=0

def Dequeue():
    global Queue, HeadPointer,TailPointer
    if HeadPointer==-1 or HeadPointer==TailPointer:
        print("queue is empty, cannot dequeue")
        return "Empty"
    else:
        HeadPointer+=1
        return Queue[HeadPointer-1]
        
def ReadData():
    try:
        myFile=open(r"PastPapers\w23p41\QueueData.txt",'r')
        while True:
            line=str(myFile.readline())
            if line=="":
                break
            else:
                Enqueue(line.strip())
        myFile.close()
    except IOError:
        print("file not found")





    
class RecordData():
    def __init__(self,ID,Total):
        self.ID=ID #ID : STRING
        self.Total=Total # Total : INTEGER

Records=[] #50 elements array of type RecordData
NumberRecords=0 #Integer



def TotalData():
    global Records,NumberRecords
    DataAccessed=Dequeue() #type STRING
    flag=False #Boolean
    if NumberRecords==0:
        Records.append(RecordData(DataAccessed,1))
        flag=True
        NumberRecords=NumberRecords+1
    else:
        for x in range(0,NumberRecords):
            if Records[x].ID==DataAccessed:
                Records[x].Total+=1
                flag=True
    if flag==False:
        Records.append(RecordData(DataAccessed,1))
        NumberRecords=NumberRecords+1


def OutputRecords():
    global Records
    for element in Records:
        print("ID ", element.ID," Total ",element.Total)

ReadData()
for element in Queue:
    TotalData()    
OutputRecords()





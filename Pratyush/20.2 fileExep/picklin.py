import pickle
import datetime

class student:
    def __init_(self):
        self.name = ""
        self.registerNumber=0
        self.dateOfBirth= datetime.date.now()
        self.fullTime=True

def CreateRecord():
    studentRecord=student()

    studentFile=open('students.DAT','wb')
    print('please enter student details ')
    studentRecord.name=input('name')
    studentRecord.registerNumber=int(input('reg number'))
    year=int(input("year"))
    month=int(input("month"))
    day=int(input("day"))
    studentRecord.dateOfBirth=datetime.date(year,month,day)
    studentRecord.fullTime=bool(input('True for full, False for part time'))
    pickle.dump (studentRecord, studentFile)

    print(studentRecord.name,studentRecord.registerNumber,studentRecord.dateOfBirth, studentRecord.fullTime)
    studentFile.close

def loadRecord():
    studentFile=open('students.DAT','rb')
    studentRecord=pickle.load(studentFile)
    print(studentRecord.name,studentRecord.registerNumber,studentRecord.dateOfBirth, studentRecord.fullTime)

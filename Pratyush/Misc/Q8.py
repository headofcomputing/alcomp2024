#another KA we did in class

import datetime
class Student():
    def __init__(self,name,dob):
        self.__StudentName=name
        self.__StudentDateOfBirth=dob

class FullTimeStudent(Student):
    def __init__(self,name,dob,address,telephoneNo):
        super().__init__(name,dob)
        self.__Address=address
        self.__TelephoneNumber=telephoneNo

NewStudent=FullTimeStudent("A. Nyone",datetime.date(1990,11,12),099111)
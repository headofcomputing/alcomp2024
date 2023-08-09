#class definition
class Lesson:
    #initialisation
    def __init__(self, LessonType, Instructor):
        self.__lessonType=LessonType
        self.__instructor=Instructor
    
    #getters
    def GetLessonType(self):
        return self.__lessonType
    
    def GetInstructor(self):
        return self.__instructor
    
    #setters
    def setLessonType(self,LessonType):
        self.__lessonType=LessonType

    def setInstructorType(self,Instructor):
        self.__instructor=Instructor

    #Other Methods
    def GetFee(self,char):
        if char=='B':
            return 45
        elif char=='I':
            return 50
        elif char=='A':
            return 55
        else:
            return -1 #returns -1 if not valid char

LessonArray=[None]*9
LessonArray[2]=Lesson("Improve Your Serve","David")


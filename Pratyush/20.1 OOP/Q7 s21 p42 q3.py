#question a
class QuizClass():
    def __init__(self):
        self.__questions=[None]*20 #Questions : ARRAY[0,19] OF QuestionClass
        self.__NumberOfQuestions=0 #NumberOfQuestion : INTEGER

    #Q b
    def AddQuestion(self,question):
        if self.__NumberOfQuestions>=20:
            return False
        else:
            self.__questions[self.__NumberOfQuestions]=question
            self.__NumberOfQuestions=self.__NumberOfQuestions+1

class QuestionClass():
    def __init__(self,question,answer,difficulty):
        self.__Question=question
        self.__Answer=answer
        self.__Difficulty=difficulty

FirstQuiz=QuizClass()
Question1=QuestionClass("What is 100 / 5 ?","20",1)
FirstQuiz.AddQuestion(Question1)
print(FirstQuiz.__dir__())

#question d -- no idea
#quesiton d -- "Containment"


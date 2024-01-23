class Picture():
    #self.__description : String
    #self.__width : Integer
    #self.__height : Integer
    #self.__frameColor : String

    def __init__(self,desc,width,height,frameColor):
        self.__description = desc
        self.__width =width
        self.__height =height
        self.__frameColor =frameColor

    def getDescription(self):
        return self.__description
    
    def getWidth(self):
        return self.__width
    
    def getHeight(self):
        return self.__height
    
    def getFrameColor(self):
        return self.__frameColor
    
    def SetDescription(self,desc):
        self.__description=desc
    
PictureArray= []
for i in range(0,100):
    PictureArray.append(Picture("",0,0,""))

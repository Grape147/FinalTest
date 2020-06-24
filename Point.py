class Point:
    __x = 0
    __y = 0
    def __init__(self):
        self.__x = 0
        self.__y = 0
    def __init__(self,a,b):
        self.__x = a
        self.__y = b
    def distance(self, other):
        length = ((self.getx() - other.getx())**2 + (self.gety() - other.gety())**2)**0.5
        print("거리는 ",length,"입니다")
        return length
    def __add__(self, other):
        hapx = self.getx()+other.getx()
        hapy = self.gety()+other.gety()
        print("(",hapx,",",hapy,")")
        return hapx, hapy
    def getx(self):
        return self.__x
    def gety(self):
        return self.__y
        
p1 = Point(1, 1)
p2 = Point(2, 2)
p1.distance(p2)
p1+p2

from abc import ABC,abstractmethod
#abstractclass
class shape(ABC):
    @abstractmethod
    def area(self):
        print('calculating the area')
class Circles(shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        print('area of circle is',3.14*self.r**2)
class Square(shape):
    def __init__(self,s):
        self.s=s
    def area(self):
        print('area of square is  ',self.s**2)
c=Circles(4)
c.area()
s=Square(6)
s.area()

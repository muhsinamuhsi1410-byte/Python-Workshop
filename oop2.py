#rectangle

class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def calculate_area(self) :
        return self.width*self.height
    def calculate_perimeter(self):
        return 2*(self.width+self.height)
r=Rectangle(5,10)
print("Area=",r.calculate_area())
print("perimeter=",r.calculate_perimeter())   
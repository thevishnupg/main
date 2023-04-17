class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def Area(self):
        area = self.width * self.height
        return area
n = int(input('Enter the widht:'))
m = int(input('Enter the height:'))

rect = Rectangle(n,m)
print(rect.Area())

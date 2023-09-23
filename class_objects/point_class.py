from math import sqrt

class Point:

    list_points = []

    def __init__(self, coord_x=0, coord_y=0):
        self.move_to(coord_x, coord_y)
        Point.list_points.append(self)

    def move_to(self,new_x,new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0,0)
    
    def print_point(self):
        print(f'point with coordinats ({self.x},{self.y})')

    def calc_distance(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError(f'Argument should be part of class Point')
        
        return sqrt((self.x - another_point.x)**2 + (self.y - another_point.y)**2)




p1 = Point(3,4)
p2 = Point(-4,34)
p3 = Point()
p5 = Point()
p5.print_point()
p5.move_to(56,34)
print(p5.print_point())
p3.move_to(98,4)
p3.move_to(98,7)
print(p3.x, p3.y)
print(p1)
print(p2.__dict__)
p7 = Point(6,0)
p8 = Point(0,8)
p9 = Point(9,8)
print(p9, Point.list_points)
print(p7.calc_distance(p8))

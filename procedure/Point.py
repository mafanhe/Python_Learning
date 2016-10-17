# -*-coding:utf-8 -*-
import copy
import math
import polygon
import turtle

class Point:
    """二维空间的点"""

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Point):
            return self.add_point(other)
        else:
            return self.add_tuple(other)

    def __radd__(self, other):
        self.__add__(other)

    def add_point(self, other):
        return Point(self.x+other.x, self.y+other.y)

    def add_tuple(self, other):
        return Point(self.x+other[0], self.y+other[1])

    def print_point(self):
        print(self.__str__())

    def move_point(self, x, y):
        self.x += x
        self.y += y


class Rectangle:
    """矩形
    属性： 角，宽度，高度
    """
    def __init__(self, c=Point(0, 0), w=0, h=0):
        self.corner = c
        self.w = w
        self.h = h

    def draw_rect(self, t):
        t.pu()
        t.goto(self.corner.x, self.corner.y)
        t.setheading(0)
        t.pd()

        for lenght in self.w, self.h, self.w, self.h:
            t.fd(lenght)
            t.rt(90)


class Circle:
    """圆
    属性： 圆心，半径
    """
    def __init__(self, c=Point(0, 0), r=0):
        self.c = copy.copy(c)
        self.r = r

    def point_in_circle(self,p):
        s = math.sqrt((self.c.x-p.x)**2+(self.c.y-p.y)**2)
        return True if s < self.r else False

    def rect_in_circle(self,rect):
        rect_point1 = rect.corner
        rect_point2 = Rectangle(rect.corner.x+rect.w, rect.corner.y)
        rect_point3 = Rectangle(rect.corner.x, rect.corner.y+rect.h)
        rect_point4 = Rectangle(rect.corner.x+rect.w, rect.corner.y+rect.h)
        if self.point_in_circle(rect_point1) and self.point_in_circle(rect_point2) and \
                self.point_in_circle(rect_point3) and self.point_in_circle(rect_point4):
            return True
        return False

    def draw_circle(self, t):
        t.pu()
        t.goto(self.c.x, self.c.y)
        t.fd(self.r)
        t.lt(90)
        t.pd()
        polygon.circle(t, self.r)


def print_attribute(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))

if __name__ == "__main__":
    yuan = Circle(Point(1, 1), 10)
    t = turtle.Turtle()
    yuan.draw_circle(t)
    turtle.mainloop()

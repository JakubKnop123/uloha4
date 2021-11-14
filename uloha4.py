import turtle
from Rectangle import Rectangle
from Triangle import Triangle
from Circle import Circle

t = turtle.Turtle()
t.speed(10)

rectangle = Rectangle(15,15,50,100)
rectangle.setColor("red")
rectangle.draw(t)

rectangle2 = Rectangle(-85,85,200,68)
rectangle2.setColor("blue")
rectangle2.draw(t)

triangle = Triangle(0,0,120)
triangle.setColor("green")
triangle.draw(t)

circle = Circle(0,0,120)
circle.setColor("orange")
circle.draw(t)

turtle.exitonclick()

from Shape import Shape

class Rectangle(Shape):
    def __init__(self, pos_x, pos_y, side_a, side_b):
        super().__init__(pos_x,pos_y)
        self.a = side_a
        self.b = side_b

    def draw(self, turtle):
        super().draw(turtle)
        if self.color != None:
            turtle.pencolor(self.color)

        for i in range(0,2):
            turtle.fd(self.a)
            turtle.right(90)
            turtle.fd(self.b)
            turtle.right(90)
class Shape:
    def __init__(self,pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y
        self.color = None

    def setColor(self, color):
        self.color = color

    def draw(self, turtle):
        turtle.penup()
        turtle.setpos(self.x, self.y)
        turtle.pendown()

from Shape import Shape

class Triangle(Shape):
    def __init__(self, pos_x, pos_y, side_a):
        super().__init__(pos_x,pos_y)
        self.a = side_a

    def draw(self, turtle):
        super().draw(turtle)
        if self.color != None:
            turtle.pencolor(self.color)

        for i in range(1):
            turtle.fd(self.a)
            turtle.left(120)
            turtle.fd(self.a)
            turtle.left(120)
            turtle.fd(self.a)
            turtle.left(120)

from Shape import Shape

class Circle(Shape):
    def __init__(self, pos_x, pos_y, side_a):
        super().__init__(pos_x, pos_y)
        self.a = side_a

    def draw(self, turtle):
        super().draw(turtle)
        if self.color != None:
            turtle.pencolor(self.color)

        for i in range(1):
            turtle.circle(self.a)






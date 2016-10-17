import polygon as pg
import turtle
import math

def rectangle(t,r,angle):
    pg.polyline(t,2,r,180-angle)




def pie(t,n,lenth):

    r=lenth/math.sin(math.pi/n)/2
    print r
    for i in range(n):
        rectangle(bob,r,360/n)
        bob.lt(360/n)
    bob.rt((180-360/n)/2)
    pg.polygon(t,n,lenth)
    

bob = turtle.Turtle()
pie(bob,3,100)
bob.hideturtle()
turtle.mainloop()

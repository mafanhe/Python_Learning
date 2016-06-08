import polygon as pg
import math
import turtle

def _d(t,length):
    t.rt(90)
    t.fd(length)
    t.lt(90)
    pg.arc(t,length/2,180)

bob = turtle.Turtle()

_d(bob,50)
_d(bob,50)
turtle.mainloop()
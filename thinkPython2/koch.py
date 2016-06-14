import turtle

def fd(t, length):
    t.fd(length)

def bk(t, length):
    t.bk(length)

def lt(t, angle=90):
    t.lt(angle)

def rt(t, angle=90):
    t.rt(angle)

def pd(t):
    t.pd()

def pu(t):
    t.pu()

def koch(t,length):
    if length<3:
        fd(t,length)
        return
    koch(t,length/3.0)
    lt(t,60)
    koch(t,length/3.0)
    rt(t,120)
    koch(t,length/3.0)
    lt(t,60)
    koch(t,length/3.0)

def snowflake(t,length):
    for i in range(3):
        koch(bob,length)
        rt(bob,120)
    
if __name__=='__main__':
    bob=turtle.Turtle()
    
    # draw a sequence of three flowers, as shown in the book.
    snowflake(bob,81)
    bob.hideturtle()
    turtle.mainloop()

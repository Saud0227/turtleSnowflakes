import snowflake as s

import turtle as t
from random import randint


wn=t.Screen()
t.hideturtle()
t.speed(0)


def snowStorm(num):
    t.pu()
    for i in range(num):
        t.setpos(randint(-t.screensize()[0]/2,t.screensize()[0]/2),randint(-t.screensize()[1]/2,t.screensize()[1]/2))
        print("drawing @ " + str(t.pos()))
        t.pd()
        s.snowflake(t, int(randint(1,2))*6, int(randint(20,40)))
        t.pu()
        t.setpos(0,0)
        print("screen " + str(wn.screensize()[0]) + " " + str(wn.screensize()[1]))



snowStorm(5)
t.mainloop()
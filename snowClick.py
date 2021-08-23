#!/usr/bin/python3
import turtle as t
from time import sleep
from random import choice, randint

import snowflake as s

wn=t.Screen()
wn.setup(400,400)



t.ht()
t.fillcolor("SKYBLUE")
t.speed(0)


#click mode:
#--------------------------------
dC = False
clickList=[]
t.pu()
def clickJustHappend(x,y):
    global dC
    clickList.append((x,y))
    if dC is False:
        dC = True
        drawShit()

    



def drawShit():
    global clickList, dC
    while len(clickList) > 0:
        t.goto(clickList[0][0],clickList[0][1])
        t.pd()
        s.snowflake(t,int(randint(1,2))*6, 20)
        t.pu()
        t.goto(0,0)
        tmpL = []
        if len(clickList) > 1:
            for i in range(1,len(clickList)):
                tmpL.append(clickList[i])
        clickList = tmpL
        sleep(1)
    dC = False

wn.onclick(clickJustHappend)
t.mainloop()

#-----------------------------------
#t.Screen().exitonclick()
"""
if len(clickList):
    print("!")
t.mainloop()
"""
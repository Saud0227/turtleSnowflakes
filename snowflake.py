#!/usr/bin/python3



def arm(t,degMod, sc):
    for i in range(5):
        t.forward(sc/5*i)
        t.right(180/degMod)
        t.forward(sc/5)
        t.backward(sc/5)
        t.left(180/degMod*2)
        t.forward(sc/5)
        t.backward(sc/5)
        t.right(180/degMod)
        t.backward(sc/5*i)

def snowflake(t,arms, s):
    print("Snowflake: \n Arms:{} , Size:{} ".format(arms,s))
    for i in range(arms):
        arm(t,arms/1.5, s)
        t.right(360/arms)


#This part only runs if the scipt is excuted as a script, not if it's used as a library
if __name__ == "__main__":
    import turtle as tu
    wn = tu.Screen()
    wn.setup(400,400)
    print("DEMO: Snowflake")

    snowflake(tu,6,40)
    tu.mainloop()

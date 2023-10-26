import turtle as trtl
import math








dino = trtl.Turtle ()
dino.speed(0.3)
dino.turtlesize(5)
#dino.hideturtle()
# chartreuse Fuchsia (Hot Pink) (GhostWhite) GreenYellow (Olive) (OliveDrab) (DarkOrchid) (Lime Green) (#c233ff) (#00cc66) (#c28af0)
#setting up drawing
# define the foot, the tail, and the blanket*
# Make tail like spikes tail
# angle 450 for big fat head












dino_colors = ['chartreuse', 'DarkOrchid' ]




def his_tail(start_x, start_y, angle):
    dino.goto(start_x, start_y)
    dino.setheading(angle)
    outline_color = dino_colors.pop(1)
    dino.pencolor(outline_color)
    dino.pensize(3)
    dino_colors.append('#c28af0')




dino.penup()
his_tail(50, -10, 330)
dino.pendown ()








# start draw tail
dino.fillcolor (dino_colors[1])
dino.begin_fill ()
dino.circle (85,100)
pos = (dino.xcor (), dino.ycor ())
'''dino.stamp() # fix
'''
dino.setheading (290)
dino.circle(-110,90)
dino.goto(50, -10)
dino.end_fill ()
















dino.penup ()
#setting up the bottom of the tail
dino.goto(pos)
dino.setheading (315)
dino.fillcolor ("#d9ffd9")
dino.begin_fill ()
dino.pencolor ("#00cc66")
dino.pendown()








dino.circle (-90, 130)
dino.setheading (-232)
dino.forward (20)
pos = (dino.xcor (), dino.ycor ())
















dino.pencolor ("#d9ffd9")
dino.setheading (13)
dino.circle (98, 98)
dino.end_fill ()








dino.pencolor ("#00cc66")
# setting up the lines on deeknows tail
# a while/if loop could work- make counter and x/y position, condition of count, set position, move and draw line, add/sub x/y pos for next line
'''
t = 1
dino.setheading (-21)
while t <= 4:
    dino.forward (30)
    dino.goto (dino.xcor () / 2,dino.ycor () / t)
    dino.setheading (-21 * t)
    t += 1
'''


#should define so bring up later easier
# setting up spike(hehe) on tail
dino.penup ()
dino.fillcolor ("#d9ffd9")
dino.pencolor ("#00cc66")
dino.goto (50, -10)
dino.goto (75, -20)
pos_for_sheet = (dino.xcor () + 8, dino.ycor () + 12) #setting up sheet for later
dino.pendown ()




# Doing the spike(hehe) on his tail
dino.begin_fill ()
dino.hideturtle ()
dino.circle(-23, 225, 2)
dino.setheading (-170)
dino.circle (-130, 18)
dino.end_fill ()




dino.showturtle ()




# need to define ghost deeknow
# getting ready to do the sheet on ghost deeknows head
dino.penup ()
dino.pencolor ("DarkOrchid")
dino.fillcolor ("GhostWhite")
dino.goto (pos_for_sheet)
dino.pendown ()
#concavity!!!!!!!!(teacher maybe said poly too) gravity, cavity, tragedy, blasphemy, taxidermy,
#bumps of his back
dino.circle (-30, 130)


# put eye code in other spot, maybe later idk
dino.fillcolor ("#00cc66")
dino.pencolor ("#00cc66")


#deeknows eye


dino.penup ()
dino.goto (-140,140)
dino.pendown ()
dino.begin_fill ()
dino.setheading (180)
dino.circle(10, -180)
dino.circle(15, -180)
dino.setheading (-160)
dino.circle (6, 180, 2)
dino.end_fill ()


# big slant lines on sheet ( closest to arm to tail)
dino.pencolor ("DarkOrchid")
dino.penup ()
dino.goto (-192, -5)
dino.pendown ()
dino.setheading (285)
dino.circle (160, 30)
dino.penup ()
dino.goto (-40, 10)
dino.pendown ()
dino.setheading (242)
dino.circle (158, 35)
dino.penup ()
dino.goto (5, 15)
dino.pendown ()
dino.setheading (242)
dino.circle (170, 40)




#ah!


















#maybe define, probably should
#deeknows toe nuggets
dino.penup ()
dino.goto (0, -200)
dino.pendown ()
dino.fillcolor ("#c28af0")
dino.begin_fill ()
toes = 1
while toes < 4:
    dino.setheading (-283)
    dino.circle (10, 200)
    toes += 1
dino.forward (5)
dino.setheading (0)
dino.forward (60)
dino.end_fill ()
#boo
dino.penup ()
dino.goto (53, 20)
dino.setheading (270)
dino.pendown ()
dino.circle (160, 40)
dino.circle (-180, 10)
dino.circle (-40, 160)












print('This is deeknow')










wn = trtl.Screen ()
wn.mainloop()

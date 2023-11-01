import turtle as trtl

dino = trtl.Turtle()
dino.speed(0.0)
dino.turtlesize(5)
dino.hideturtle()
naked_deeknow = True
blinky_deeknow = False
# chartreuse Fuchsia (Hot Pink) (GhostWhite) GreenYellow (Olive) (OliveDrab) (DarkOrchid) (Lime Green) (#c233ff) (#00cc66) (#c28af0)
# setting up drawing
# Make tail like spikes tail


# MEMBER MUST MOVE!!


dino_colors = ['chartreuse', 'DarkOrchid' ]

# deeknows tail
def his_tail(start_x, start_y, angle):
    dino.goto(start_x, start_y)
    dino.setheading(angle)
    outline_color = dino_colors.pop(1)
    dino.pencolor(outline_color)
    dino.pensize(3)
    dino_colors.append('#c28af0')

dino.penup()
his_tail(50, -10, 330)
dino.pendown()

# start draw tail
dino.fillcolor(dino_colors[1])
dino.begin_fill()
dino.circle(85,100)
pos = (dino.xcor(), dino.ycor())
dino.setheading(290)
dino.circle(-110,90)
dino.goto(50, -10)
dino.end_fill()

# setting up the bottom of the tail
dino.penup()
dino.goto(pos)
dino.setheading(315)
dino.fillcolor("#d9ffd9")
dino.begin_fill()
dino.pencolor("#00cc66")
dino.pendown()


dino.circle(-90, 130)
dino.setheading(-232)
dino.forward(20)
pos = (dino.xcor(), dino.ycor())


dino.pencolor("#d9ffd9")
dino.setheading(13)
dino.circle(98, 98)
dino.end_fill()

# setting up the lines on deeknows tail
dino.pencolor ("#00cc66")
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
# setting up spike(hehe) on tail
dino.penup()
dino.fillcolor("#d9ffd9")
dino.pencolor("#00cc66")
dino.goto(50, -10)
dino.goto(75, -20)
pos_for_sheet = (dino.xcor() + 8, dino.ycor() + 12) # setting up sheet for later
dino.pendown()

# Doing the spike(hehe) on his tail
dino.begin_fill()
dino.hideturtle()
dino.circle(-23, 225, 2)
dino.setheading(-170)
dino.circle(-130, 18)
dino.end_fill()

# leg day
dino.penup()
dino.goto(0, -200)
dino.pendown()
dino.pencolor('DarkOrchid')
dino.fillcolor('#c28af0')
dino.begin_fill()
dino.setheading(0)
dino.circle(10, 45)
dino.setheading(90)
dino.forward(50)
dino.setheading(90)
dino.circle(10, 45)
dino.setheading(180)
dino.forward(65)
dino.circle(10, 45)
dino.setheading(270)
dino.forward(50)
dino.circle(10, 45)
dino.setheading(0)
dino.forward(5)
dino.end_fill()

# deeknows toe nuggets set up
# toes code
dino.fillcolor("fuchsia")
dino.begin_fill()
dino.goto(0, -200)
toes = 1
while toes < 4:
    dino.setheading(-283)
    dino.circle(10, 200)
    toes += 1

# gotta give him legs
pos = (dino.xcor() + 10, dino.ycor() - 5)
dino.forward(5)
dino.setheading(0)
dino.forward(60)
dino.end_fill()

# ghost deeknow
def GhostDeeknow():
    dino.penup()
    dino.pencolor("Grey")
    dino.fillcolor("GhostWhite")  
    dino.goto(pos_for_sheet)
    dino.setheading(180)
    dino.pendown()
    # if blinky_deeknow == True:
    if naked_deeknow == False:
        dino.pencolor('firebrick')
        dino.fillcolor('fuchsia')
    # call deeknow outline
    Deeknow_outline()

# deeknow outline start by tail
def Deeknow_outline():
    # called in ghost deeknow
    dino.begin_fill()
    dino.circle(-50, 130)
    dino.setheading(62)
    dino.circle(5, 130)
    dino.setheading(180)
    dino.forward(30)
    dino.circle(-10, 150)
    dino.forward(20)
    dino.circle(20, 70)
    dino.setheading(150)
    dino.forward(20)
    dino.circle(-20, 120)
    dino.forward(10)
    dino.circle(12, 120)
    dino.setheading(160)
    dino.forward(15)
    dino.circle(-10, 75)
    dino.setheading(80)
    dino.forward(30)
    dino.circle(20, 120)
    dino.forward(30)
    dino.setheading(185)
    dino.forward(20)
    # extra line going the other way
    dino.setheading(310)
    dino.forward(35)
    dino.backward(35)
    dino.setheading(130)
    dino.forward(35)
    dino.circle(10, 45)
    dino.setheading(200)
    dino.forward(15)
    dino.setheading(230)
    dino.forward(30)
    dino.setheading(195)
    # forehead
    dino.forward(50)
    dino.setheading(200)
    dino.forward(60)
    dino.setheading(210)
    dino.circle(40, 10)
    dino.setheading(250)
    dino.circle(150, 50)
    # low jaw
    dino.setheading(345)
    dino.forward(70)
    dino.setheading(340)
    dino.forward(30)
    dino.setheading(325)
    dino.forward(20)
    pos_slant_start = (dino.xcor() + 10, dino.ycor())
    dino.backward(20)
    dino.setheading(340)
    dino.backward(10)
    dino.setheading(250)
    dino.circle(-30, 80)
    dino.circle(30, 105)
    dino.forward(60)
    dino.backward(20)
    dino.setheading(250)
    dino.forward(15)
    dino.setheading(255)
    dino.forward(30)
    dino.setheading(250)
    dino.forward(30)
    dino.setheading(240)
    dino.forward(20)
    dino.circle(5, 140)
    dino.forward(20)
    dino.circle(-50, 75)
    dino.forward(40)
    dino.circle(50, 70)
    dino.circle(30, 45)
    dino.forward(15)
    dino.circle(-20, 60)
    dino.forward(33)
    dino.circle(-10, 80)
    dino.forward(10)
    dino.circle(10, 45)
    dino.circle(70, 100)
    dino.circle(50, 70)
    dino.forward(20)
    dino.setheading(125)
    dino.forward(30)
    dino.setheading(120)
    dino.forward(20)
    dino.setheading(110)
    dino.forward(20)
    dino.setheading(120)
    dino.forward(10)
    dino.end_fill()
    dino.penup()
    dino.goto(pos_slant_start)
    sheet_slant_lines()

def sheet_slant_lines():
    dino.pendown()
    # arm slant
    dino.setheading(250)
    dino.circle(-50, 45)
    dino.forward(20)
    dino.setheading(200)
    dino.forward(15)
    dino.setheading(190)
    dino.forward(10)
    dino.setheading(250)
    dino.circle(120, 45)
    # slant right next to arm
    dino.penup()
    dino.goto(dino.xcor()-5, dino.ycor() + 54)
    dino.pendown()
    dino.setheading(280)
    dino.circle(140, 40)
    # small line at the bottom
    dino.penup()
    dino.goto(dino.xcor() + 15, dino.ycor() - 15)
    dino.pendown()
    dino.setheading(320)
    dino.circle(-50, 50)
    # other random slant lines on sheet
    dino.penup()
    dino.goto(-45, 20)
    dino.pendown()
    dino.setheading(243)
    dino.circle(230, 35)
    dino.penup()
    dino.goto(0, 30)
    dino.pendown()
    dino.setheading(260)
    dino.circle(250, 15)
    dino.forward(55)
    dino.circle(250, 10)
    naked_deeknow = False
    deeknows_eye()

def deeknows_eye():
    # deeknows eye
    dino.fillcolor("#00cc66")
    dino.pencolor("#00cc66")
    dino.penup()
    dino.goto(-110,200)
    dino.pendown()
    dino.begin_fill()
    dino.setheading(180)
    dino.circle(10, -180)
    dino.circle(15, -180)
    dino.setheading(-160)
    dino.circle(6, 180, 2)
    dino.end_fill()

GhostDeeknow()

# ah!

'''
if naked_deeknow == True:
    GhostDeeknow()
else:
    while naked_deeknow == False:
        #call def for tail wag/color
        blinky_deeknow = True
        #dino.clear()
        GhostDeeknow()
'''

print('This is deeknow')

wn = trtl.Screen()
wn.mainloop()

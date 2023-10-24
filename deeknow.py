#   deeknow.py
#   making a scary dinosaur
"""Module providing a function something something."""
import turtle as trtl

dino = trtl.Turtle()
dino.speed(0)
dino.turtlesize(5)
# dino.hideturtle()
# Fuchsia  (Hot Pink) (GhostWhite) GreenYellow (Olive) (OliveDrab)
# light green(#c233ff)and(#00cc66), purple(#c28af0), under tail(#d9ffd9)
# setting up drawing
# define the foot, the tail, and the blanket*
# Make tail like spikes tail
# angle 450 for big fat head

dino_colors = ['#d9ffd9', 'DarkOrchid']

# spider.clear() erases the spider completely
# Then can call draw again to make other spider
# can use to make movement or tiny dino or color dino or blink dino
# .dot(s) to make his eye s = diameter
# draw lower tail first using upper tail and lower tail code
# then draw upper tail so there's no overlap

def his_tail(start_x, start_y):
    """Module providing a function to draw his tail."""
    angle = 330
    dino.goto(start_x, start_y)
    dino.setheading(angle)
    outline_color = dino_colors.pop(1)
    dino.pencolor(outline_color)
    dino.pensize(3)
    dino_colors.append('#c28af0')
    # start draw tail
    # this is outline to perimeter of tail after fillcolor for upper tail
    dino.pencolor('chartreuse')
    dino.fillcolor(dino_colors[-1])
    dino.begin_fill()
    dino.circle(85, 100)
    first_circle_xy = (dino.xcor(), dino.ycor())
    # stamp later so outline not on top
    # dino.left(10)
    # dino.forward(23)
    # dino.stamp()
    # dino.goto(first_circle_xy)
    dino.setheading(290)
    dino.circle(-110, 90)
    # second_circle_xy = (dino.xcor(), dino.ycor())
    dino.goto(start_x, start_y)
    dino.end_fill()
    # lower tail
    dino.penup()
    #
    dino.goto(first_circle_xy)
    dino.setheading(310)
    #
    dino.pendown()
    #
    dino.fillcolor('#d9ffd9')
    dino.begin_fill()
    dino.circle(-110, 115)
    dino.end_fill()  # put pen up and down to break line
    # triangle tail
    dino.goto(start_x, start_y)  # not right end spot
    dino.fillcolor('chartreuse')
    dino.begin_fill()
    dino.setheading(angle)
    dino.circle(85, 55)
    dino.setheading(100)
    dino.circle(30, 169, 2)
    dino.end_fill()


dino.penup()
his_tail(50, -10)
dino.pendown()

# dino.clone?

print('This is dino')

WN = trtl.Screen()
WN.mainloop()

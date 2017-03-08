'''
Using the turtle library, create a fractal pattern.
You may use heading/forward/backward or goto and fill commands to draw
your fractal.  Ideas for your fractal pattern might include
examples from the chapter.  You can find many fractal examples online,
but please make your fractal unique.  Experiment with the variables
to change the appearance and behavior.

Give your fractal a depth of at least 5.  Ensure the fractal is contained on the screen (at whatever size you set it).  Have fun.
(35pts)
'''

import turtle
import math

my_turtle=turtle.Turtle()
my_screen=turtle.Screen()
color_list=["red","orange","yellow","green","blue","purple","magenta","cyan","black"]

def draw(x,y,heading,dist,depth):
    my_turtle.up()
    my_turtle.goto(x,y)
    my_turtle.color("black")
    my_turtle.down()
    my_turtle.setheading(heading)
    my_turtle.forward(dist)

    new_y=my_turtle.ycor()
    new_x=my_turtle.xcor()
    if depth>0:
        for i in range(1,4):
            draw(new_x,new_y,heading+45,dist/i,depth-1)
            draw(new_x,new_y,heading-45,dist/i*(math.pi/3),depth-1)

my_turtle.speed(10)
for i in range(720):

    my_turtle.setheading(math.pi+10*i)
    my_turtle.forward(1+0.006*i)
my_turtle.goto(-5,5)
for i in range(1,1440,10):

    my_turtle.setheading(math.pi*20*i)
    my_turtle.forward(-i*1/2)
for i in range(1,720,10):
    draw(0,0,i,-i*1/2,1)

my_screen.exitonclick()
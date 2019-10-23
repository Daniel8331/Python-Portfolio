#Daniel Embley
#Turtle Project
#10/11



import turtle 
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
t = turtle.Pen()
t.speed(0)
turtle.bgcolor('black') 
for x in range(360): 
    t.pencolor(colors[x%6]) 
    t.width(x/100 + 1) 
    t.forward(x) 
    t.left(59) 

##from turtle import *
##
##from random import randint
##
##bgcolor('black')
##
##x = 1
##
##while x < 400:
##
##    r = randint(0,225)
##    g = randint(0,225)
##    b = randint(0,225)
##
##    colormode (225)
##
##
##    pencolor(r,g,b)
##
##
##    fd (50 + x)
##    rt (90.911)
##
##
##    x = x+1
##
##exitonclick()
##
##
##
##



##speed (0)
##turtle.setup (width = 1000, height = 1000)
##x = turtle.Pen()
##x.shape("turtle")
##x.color("black")
##x.speed(0)
##x.width(1)
##
##x.pencolor("black")
##
##for i in range(50):
##    x.forward(50)
##    x.left(123)
##
##x.pencolor("red")
##
##for i in range(

##x.up()
##x.setposition(150,150)
## 
##x = turtle.Turtle()
##x.down()
##x.begin_fill ()
##x.forward(100)
##x.left(90)
##x.forward(100)
##x.left(90)
##x.forward(100)
##x.left(90)
##x.forward(100)
##x.left(90)
##x.end_fill()
##x.reset()
##
##x.speed(0)
##for i in range(5):
##    x.forward(100)
##    x.right(144)
##for i in range(8):
##    x.forward(100)
##    x.left(225)
##y = turtle.Pen()
##y.shape("turtle")
##y.color("black")
##y.speed(1)
##y.width(5)
##
##y.up
##y.setposition(-150, -150)
##y.down()
##
##y.begin_fill ()
##y.forward(100)
##y.right(90)
##y.forward(100)
##y.right(90)
##
##y.forward(100)
##y.right(90)
##y.forward(100)
##y.right(90)
##y.end_fill()

from contextlib import redirect_stderr
from turtle import *

speed(10)


color("black")
width(7)
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(70)
left(90)

color("yellow")
forward(90)
right(90)

forward(50)
right(90)

forward(90)

penup()
goto(200,200)
pendown()

color("brown")
begin_fill()
right(150)
forward(190)

left(118)
forward(190)
end_fill()

penup()
goto(140, 160)
pendown()

color("orange")
begin_fill()
left(28)
forward(40)
left(92)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
end_fill()


penup()
goto(20,120)
pendown()

left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)

left(180)
forward(25)
right(90)
forward(40)
left(180)
forward(20)
right(90)
forward(15)


exitonclick()
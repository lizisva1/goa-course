from turtle import *
#we want to paint a house

#step 1: draw a square
speed(35)

width(7)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door 
forward(70)
color("green")
left(90)
forward(120)     #height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

color("green")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#sun
penup()
goto(-200, 125)
pendown()
color("yellow")
begin_fill()
circle(35)
end_fill()


exitonclick()
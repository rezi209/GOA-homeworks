from turtle import *



#we want to paint a house

#step 1: draw a square
width(7)
color("purple")  #color of house
begin_fill()
forward(200)
left(90)
end_fill() 




forward(200)     
left(90)      

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()



penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("yellow")
begin_fill()
left(50)
right(20)
forward(50)
left(90)
forward(50)
right(270)
forward(50)
left(90)
forward(50)
left(180)
forward(50)
end_fill()



color("purple")
forward(100)




color("yellow")
begin_fill()
forward(50)
right(180)
left(90)
forward(50)
right(90)
forward(50)
left(90)
right(180)
forward(50)
end_fill()



exitonclick()
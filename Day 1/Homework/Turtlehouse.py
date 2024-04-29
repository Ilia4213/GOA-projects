from turtle import *


speed(5)
width(5) 

# square
color("yellow")
penup()
goto(-100, -100)
pendown()
begin_fill()
forward(200)  
left(90)
forward(150)  
left(90)
forward(200)  
left(90)
forward(150)  
end_fill()

# roof
penup()
goto(-100, 50)
pendown()
color("red")
begin_fill()
left(150)
forward(200)  
right(120)
forward(200)  
end_fill() 

# door
color("brown")
penup()
goto(-25, -100)
pendown()
begin_fill()
left(60)
forward(50)  
left(90)
forward(75)  
left(90)
forward(50)  
left(90)
forward(75)  
end_fill()


# window
color("cyan")
penup()
goto(-75, -20)
pendown()
begin_fill()
left(90)
forward(40)  
left(90)
forward(40)  
left(90)
forward(40)  
left(90)
forward(40)  
end_fill()


# second window
penup()
goto(35, -20)
pendown()
begin_fill()
left(90)
forward(40)  
left(90)
forward(40)  
left(90)
forward(40)  
left(90)
forward(40)  
end_fill()

exitonclick()


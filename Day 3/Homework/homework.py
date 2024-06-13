from turtle import *
print('ოჯახის წევრები: თამარ მაღრაძე, გიორგი ლომიტაშვილი და მედეა ლომიტაშვილი.')


speed(100)
width(5)
bgcolor('cyan')

#Creating function for drawing a house

def house():
    color('yellow')
    begin_fill()
    
    for i in range(4):
        forward(200)
        left(90)
    
    end_fill()    
    penup()
    left(90)
    forward(200)
    pendown()
    begin_fill()
    color('brown')
    right(45)
    forward(148)
    right(90)
    forward(148)
    right(135)
    forward(200)
    end_fill()
    penup()
    backward(30)
    left(90)
    forward(50)
    pendown()
    color('cyan')  
    begin_fill()

    for i in range(2):
        forward(60)
        left(90)
        forward(40)
        left(90)

    end_fill()

    penup()
    forward(150)
    left(90)
    forward(100)
    color('brown')
    begin_fill()
    left(90)

    for i in range(2):
        forward(60)
        left(90)
        forward(40)
        left(90)

    end_fill()    

#Creating function for drawing a tree
def tree():
    pendown()
    color('darkgreen')
    begin_fill()
    circle(25)
    end_fill()
    width(15)
    right(90)
    color('brown')
    forward(40)


#Ground
penup()

goto(-480,-398)

pendown()
color('green')
begin_fill()
forward(953)
left(90)
forward(350)
left(90)
forward(953)
left(90)
forward(350)
end_fill()

penup()
color('black')
goto(-250,-150)
left(90)

house()

penup()

goto(200,-300)

right(90)

house()

goto(-10,-100)

right(90)

tree()

penup()

goto(-300,-300)

left(90)

tree()

































exitonclick()
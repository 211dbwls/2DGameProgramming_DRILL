import turtle

row = 6
while(row > 0):
    turtle.forward(500)
    turtle.left(180)
    turtle.penup()
    turtle.forward(500)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.pendown()
    row = row - 1

turtle.penup()
turtle.left(90)
turtle.forward(100)
turtle.pendown()

col = 6
while(col > 0):
    turtle.forward(500)
    turtle.right(180)
    turtle.penup()
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(-100)
    turtle.right(90)
    turtle.pendown()
    col = col - 1

turtle.exitonclick()

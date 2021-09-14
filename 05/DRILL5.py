import turtle

def wmove():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def amove():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def smove():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def dmove():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()

turtle.shape("turtle")

turtle.onkey(wmove,  'w')
turtle.onkey(amove,  'a')
turtle.onkey(smove,  's')
turtle.onkey(dmove,  'd')
turtle.onkey(restart, 'Escape')
turtle.listen()

turtle.exitonclick()

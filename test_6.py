#Virus

import turtle

a = 0
b = 1

turtle.bgcolor("Black")
turtle.speed(0)
turtle.pencolor("Green")
turtle.penup()
turtle.goto(0, 300)
turtle.pendown()

while True:
    turtle.forward(a)
    turtle.right(b)
    a += 2
    b += 2
    if b ==300:
        break
    
turtle.exitonclick()
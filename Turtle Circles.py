import turtle
# Making a program which uses Turtle to draw small colorful circles across the screen


def circles(color, width):          # This takes circle color and thickness as parameter so i can change as desired
    turtle.color('grey', color)
    turtle.pensize(width)
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.hideturtle()

turtle.speed('slowest')
turtle.penup()
turtle.setposition(-200, 200)
turtle.pendown()
circles('blue', 10)
turtle.penup()
turtle.setposition(10, 50)
turtle.pendown()
circles('purple', 5)




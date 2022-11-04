import random
import turtle

turtle.speed(1000)
turtle.hideturtle()

def starmaker(step, angle):
    for iter in range(10):
        turtle.forward(step)
        turtle.right(angle)

for i in range(20):
    if i%2==0:
        turtle.color("black")
        turtle.bgcolor("light blue")

        turtle.penup()
        turtle.setpos(random.randint(-350, 350), random.randint(100, 300))
        turtle.pendown()
        starmaker(10, 144)
    else:
        turtle.color("pink")
        turtle.bgcolor("orange")

        turtle.penup()
        turtle.setpos(random.randint(-350, 350), random.randint(100, 300))
        turtle.pendown()
        starmaker(10, 144)


turtle.exitonclick()
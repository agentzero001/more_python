import turtle as t
import random

# Set up the Turtle window
t.speed(0)
t.bgcolor("black")
t.pensize(2)

# Define a function to draw a colorful flower
def draw_flower():
    for _ in range(36):
        t.color("red")
        t.forward(100)
        t.right(45)
        t.color("orange")
        t.forward(60)
        t.right(45)
        t.color("yellow")
        t.forward(80)
        t.right(45)
        t.color("pink")
        t.forward(50)
        t.right(45)
        t.penup()
        t.setposition(0, 0)
        t.pendown()
        t.right(10)

# Draw the colorful flower
t.penup()
t.goto(0, -200)
t.pendown()
draw_flower()

# Draw the flower's stem
t.penup()
t.goto(0, -200)
t.pendown()
t.color("green")
t.pensize(5)
t.setheading(90)
t.forward(250)

# Hide the Turtle
t.hideturtle()

# Keep the window open
t.done()

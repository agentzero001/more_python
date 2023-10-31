import turtle as t


t.speed(100)
t.bgcolor("black")
t.pensize(2)
t.color("red")


t.penup()
t.goto(0, -100)
t.pendown()
t.speed(1)
t.begin_fill()
t.fillcolor("orange")
t.left(140)
t.forward(224)
t.speed(1000)
for _ in range(200):
    t.right(1)
    t.forward(2)
t.left(120)
for _ in range(200):
    t.right(1)
    t.forward(2)

t.speed(1)
t.forward(224)
t.end_fill()

# Hide the Turtle
t.hideturtle()

# Keep the window open
t.done()
4.
import turtle
import random
t = turtle.Turtle()
t.shape("turtle")
def draw_square(x, y, c):
    t.up()
    t.goto(x, y)
    t.down()
    t.color("black",c)
    t.begin_fill()
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.end_fill()

    
for c in ["yellow", "red", "purple", "blue"]:
   x = random.randint(-100, 100)
   y = random.randint(-100, 100)
   draw_square(x, y, c)
5.
import turtle
import random
t = turtle.Turtle()
s = turtle.Screen()
def draw_shape(t, c, length, sides, x, y):
    t.up()
    t.goto(x, y)
    t.down()
    t.fillcolor(c)
    angle = 360.0 / sides
    t.begin_fill()
    for dist in range(sides):
        t.forward(length)
        t.left(angle)
    t.end_fill()

    
for i in range(10):
    color = random.choice([ 'white', 'yellow', 'blue', 'skyblue', 'orange', 'green' ])
    side_length = random.randint(10, 100)
    sides = random.randint(3, 10)
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    draw_shape(t, color, side_length, sides, x, y)
 6.

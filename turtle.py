4.
import turtle                 # 터틀 라이브러리 불러옴
import random                 # 랜덤 라이브러리 불러옴
t = turtle.Turtle() 
t.shape("turtle")
def draw_square(x, y, c):     # 사각형 그리기
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
import turtle                  # 터틀 라이브러리 불러옴
import random                  # 랜덤 라이브러리 불러옴
t = turtle.Turtle()            
s = turtle.Screen()
def draw_shape(t, c, length, sides, x, y):
    t.up()
    t.goto(x, y)               # 좌표이동
    t.down()
    t.fillcolor(c)             # 색선정
    angle = 360.0 / sides
    t.begin_fill()
    for dist in range(sides):
        t.forward(length)
        t.left(angle)
    t.end_fill()

    
for i in range(10):
    color = random.choice([ 'white', 'yellow', 'blue', 'skyblue', 'orange', 'green' ])  # 색 리스트
    side_length = random.randint(10, 100)
    sides = random.randint(3, 10)
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    draw_shape(t, color, side_length, sides, x, y)
 6.
import turtle
import random
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
def draw_star(aturtle, colour,length, x, y):
    t.color(color)
    t.begin_fill()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for i in range(5):                   #  5번 반복 도형그리기
        t.forward(length)
        t.right(144)
        t.forward(length)
    t.end_fill()

    
for i in range(20):                        # 별20개 그리기
    color = random.choice([ 'white', 'yellow', 'blue', 'skyblue', 'orange', 'green' ])
    side_length = random.randint(10, 100)
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    draw_star(t, color, side_length, x, y)

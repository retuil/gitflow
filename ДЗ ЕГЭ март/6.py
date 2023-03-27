from turtle import *


n = 15
speed(10**9)
for x in range(-50, 50):
    up()
    goto(x*n, -50*n)
    down()
    goto(x*n, 50*n)
for y in range(-50, 50):
    up()
    goto(-50*n, y*n)
    down()
    goto(50*n, y*n)
up()
home()
color('red')
speed(20)
down()

for i in range(4):
    forward(10*n)
    right(270)
up()
forward(3*n)
right(270)
forward(5*n)
right(90)
down()
for i in range(2):
    forward(10*n)
    right(270)
    forward(12*n)
    right(270)
exitonclick()
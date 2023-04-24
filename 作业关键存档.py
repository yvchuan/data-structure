'''
#绘制奥运五环

import turtle
radius=int(input())
turtle.width(5)
turtle.color("red")
turtle.circle(radius)
turtle.penup()

turtle.goto(120,0)
turtle.pendown()

turtle.color("blue")
turtle.circle(radius)
turtle.penup()


turtle.goto(240,0)
turtle.pendown()

turtle.color("green")
turtle.circle(radius)
turtle.penup()

turtle.goto(60,-50)
turtle.pendown()

turtle.color("yellow")
turtle.circle(radius)
turtle.penup()

turtle.goto(180,-50)
turtle.pendown()

turtle.color("black")
turtle.circle(radius)
turtle.done()

'''




import turtle as t
r=eval(input())
t.pensize(10)
t.penup()
t.seth(180)
t.fd(400)
t.seth(90)
t.fd(200)
t.pendown()
def y():
    t.penup()
    t.seth(0)
    t.fd(2*r+20)
    t.seth(90)
    t.pendown()
def k():
    t.penup()
    t.seth(180)
    t.fd(5 * r + 50)
    t.seth(-90)
    t.fd(r)
    t.seth(90)
    t.pendown()
for i  in range(5):
    if i==0:
        t.pencolor("red")
        t.circle(-r)
        y()
    elif i==1:
          t.pencolor("blue")
          t.circle(-r)
          y()
    elif i==2:
        t.pencolor("green")
        t.circle(-r)
        y()
    elif i==3:
        t.pencolor("yellow")
        k()
        t.circle(-r)
        y()
    elif i==4:
        t.pencolor("black")
        t.circle(-r)
t.done()




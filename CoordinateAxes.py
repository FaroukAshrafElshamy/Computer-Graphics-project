from turtle import *
""" This file is to create the outline of drawing window """

# Color Mode
Color_Mode = "dark"

if Color_Mode == "light":
    BackgroundColor = "#E5E5CB"
    LinesColor = "#D5CEA3"
    AxesColor = "#3C2A21"
    DotColor = "#543526"

else:
    BackgroundColor = "#1A120B"
    LinesColor = "#3C2A21"
    AxesColor = "#D5CEA3"
    DotColor = "#DB8A62"


def coordinate(n, pixel):
    global s
    s = Screen()
    s.clear()
    s.tracer(0)
    s.setup(n, n)
    s.bgcolor(BackgroundColor)

    # Turtle
    t = Turtle()
    t.shapesize(1.5)
    t.color(LinesColor)

    t.up()
    l = n / 2
    t.goto(-l, l)
    t.down()
    t.hideturtle()

    # Squares
    for i in range(int(n / pixel / 2)):
        t.fd(n)
        t.rt(90)
        t.fd(pixel)
        t.rt(90)
        t.fd(n)
        t.lt(90)
        t.fd(pixel)
        t.lt(90)
    t.goto(-l, l)
    for i in range(int(n / pixel / 2)):
        t.rt(90)
        t.fd(n)
        t.lt(90)
        t.fd(pixel)
        t.lt(90)
        t.fd(n)
        t.rt(90)
        t.fd(pixel)

    # coordinate axes
    t.up()
    t.goto(0, 0)
    t.down()
    t.pensize(3)
    t.color(AxesColor)
    t.fd(l - 20)
    t.stamp()
    t.lt(180)
    t.fd(n - 40)
    t.stamp()
    t.home()
    t.rt(90)
    t.fd(380)
    t.stamp()
    t.lt(180)
    t.fd(760)
    t.stamp()
    t.home()
    t.hideturtle()
    s.update()

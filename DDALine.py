from CoordinateAxes import *


def dda():
    # file includes points of the circle
    file = open("DDApoints.txt", "a")
    file.truncate(0)

    n = 800
    pixel = 25
    # Coordinate Axes
    coordinate(n, pixel)

    # Turtle
    t = Turtle()
    t.color("white", "black")
    t.speed(1)
    t.hideturtle()

    # Draw dot
    def Plot(x, y):
        t.up()
        t.goto(x, y)
        t.down()
        t.dot(20, DotColor)

    # DDA Algorithm
    def DDA(x1, y1, x2, y2):
        tracer(1)
        Plot(x1 * pixel, y1 * pixel)
        file.write(f"Octect (x,y)   ({x1},{y1})\n")
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        steps = max(dx, dy)
        xinc = dx / steps
        yinc = dy / steps
        x = float(x1)
        y = float(y1)
        for i in range(steps):
            x = x + xinc
            y = y + yinc
            Plot(round(x) * pixel, round(y) * pixel)
            file.write(f"Octect (x,y)   ({round(x)},{round(y)})\n")

    # Input Coordinate
    x1 = int(textinput("Scan conversion", "Enter x1"))
    y1 = int(textinput("Scan conversion", "Enter y1"))
    x2 = int(textinput("Scan conversion", "Enter x2"))
    y2 = int(textinput("Scan conversion", "Enter y2"))
    DDA(x1, y1, x2, y2)
    file.close()
    done()

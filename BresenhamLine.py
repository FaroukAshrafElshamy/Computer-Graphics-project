from CoordinateAxes import *

def bresenhamLine():
    file = open("BerensenhamLinePoints.txt",'a')
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

    # Bresenham Line
    def Bresenham_Line(x1, y1, x2, y2):
        X = x1
        Y = y1
        file.write(f"Octect (x,y)   ({X},{Y})\n")
        dx = x2 - x1
        dy = y2 - y1
        p = (2*dy) - dx

        while X < x2:
            if p < 0:
                X += 1
                tracer(1)
                Plot(X*pixel, Y*pixel)
                file.write(f"Octect (x,y)   ({X},{Y})\n")
                p += 2 * dy
            else:
                X += 1
                Y += 1
                Plot(X*pixel, Y*pixel)
                file.write(f"Octect (x,y)   ({X},{Y})\n")
                p += (2*dy) - (2*dx)

    # Input Coordinate
    x1 = int(textinput("Scan conversion", "Enter x1"))
    y1 = int(textinput("Scan conversion", "Enter y1"))
    x2 = int(textinput("Scan conversion", "Enter x2"))
    y2 = int(textinput("Scan conversion", "Enter y2"))
    Bresenham_Line(x1, y1, x2, y2)
    file.close()
    done()
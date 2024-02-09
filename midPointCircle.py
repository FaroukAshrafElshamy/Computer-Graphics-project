from CoordinateAxes import *

def mid():
    n = 850
    pixel = 25

    # Screen
    coordinate(n,pixel)

    # file includes points of the circle
    file = open("MidPointCirclePoints.txt",'a')
    file.truncate(0)

    def plot(x , y):
        
        file.write(f"Octect (x,y)   ({x},{y})\n")
        t2.setpos( x,  y);t2.stamp();t2.color("red")
        file.write(f"Octect (y,x)   ({y},{x})\n")
        t2.setpos( y,  x);t2.stamp();t2.color("pink")

        file.write(f"Octect (y,-x)  ({y},{-x})\n")
        t2.setpos( y, - x);t2.stamp();t2.color("cyan")
        file.write(f"Octect (x,-y)  ({x},{-y})\n")
        t2.setpos( x, - y);t2.stamp();t2.color("black")

        file.write(f"Octect (-x,-y) ({-x},{-y})\n")
        t2.setpos(- x, - y);t2.stamp();t2.color("gray")
        file.write(f"Octect (-y,-x) ({-y},{-x})\n")
        t2.setpos(- y, - x);t2.stamp();t2.color("cyan")


        file.write(f"Octect (-y,x)  ({-y},{x})\n")
        t2.setpos(- y,  x);t2.stamp();t2.color("brown")
        file.write(f"Octect (-x,y)  ({-x},{y})\n")
        t2.setpos(- x,  y);t2.stamp();t2.color("blue")

    # algorithm
    def midpoint(radius):
        x,y,p = 0,radius,1-radius
        plot(x,y)
        while x<y:
            x+=1*pixel
            if p < 0 :
                plot(x,y)
                p += 2 * x + 3
            else:
                plot(x,y)
                y -= 1*pixel
                p += 2 * (x-y) + 5

    # Input 
    radius = int(textinput("Scan conversion", "Enter the radius "))

    # Text
    t1 = Turtle()
    t1.color("#fff")
    t1.hideturtle()
    t1.pu()
    t1.setpos(-420,400)
    t1.pensize(5)
    t1.write("Mid point circle drawing algorithm",False,"left",("Arial",16,"bold"))
    t1.setpos(-420,370)
    t1.write(f"Circle radius = {radius}",False,"left",("Arial",16,"bold"))

    # pixels
    tracer(1)
    t2= Turtle("circle");t2.speed(9)
    t2.shapesize(1)
    t2.pu()

    midpoint(radius)
    file.close()
    mainloop()

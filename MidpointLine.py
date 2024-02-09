from CoordinateAxes import *

def midLine():
	# file includes points of the circle
	file = open("MidPointLinePoints.txt",'a')
	file.truncate(0)

	n = 800
	pixel = 25
	# Coordinate Axes
	coordinate(n, pixel)

	# Turtle
	t = Turtle()
	t.color("white", "black")
	t.speed(10)
	t.hideturtle()

	# Draw dot
	def Plot(x, y):
		t.up()
		t.goto(x, y)
		t.down()
		t.dot(20, DotColor)

	# Midpoint Line Algorithm
	def midPoint(X1,Y1,X2,Y2): 
		dx = X2 - X1 
		dy = Y2 - Y1 

		# initial value of decision parameter d 
		d = dy - (dx/2) 
		x = X1 
		y = Y1 

		tracer(1)
		Plot(x*pixel, y*pixel) 
		file.write(f"Octect (x,y)   ({x},{y})\n")
		# iterate through value of X 
		while (x < X2): 
			x=x+1
			if(d < 0): 
				d = d + dy 
			else: 
				d = d + (dy - dx) 
				y=y+1

			Plot(x*pixel, y*pixel) 
			file.write(f"Octect (x,y)   ({x},{y})\n")

	x1 = int(textinput("Scan conversion", "Enter x1"))
	y1 = int(textinput("Scan conversion", "Enter y1"))
	x2 = int(textinput("Scan conversion", "Enter x2"))
	y2 = int(textinput("Scan conversion", "Enter y2"))
	midPoint(x1, y1, x2, y2) 
	file.close()
	done()
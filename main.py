import ttkbootstrap as ttk
from midPointCircle import *
from BresenhamCircle import *
from BresenhamLine import *
from MidpointLine import *
from DDALine import *
from snakegame import *

# algorithm
def refresh():
    Turtle_frame = ttk.Frame(window, style="light")
    Turtle_frame.pack(side="bottom")
    Turtle_frame.propagate(False)
    canvas = ttk.Canvas(Turtle_frame, width=1500, height=700)

    screen = TurtleScreen(canvas)
    t = RawTurtle(screen)
    t.clear()
    canvas.pack()
    t.speed(0)
    t.hideturtle()
    window.update()

# main window
window = ttk.Window(themename="superhero")
window.title("Graphical studing")
window.geometry("1500x500")
window.position_center()

image = ttk.PhotoImage(file="img.png")
canvas = ttk.Canvas(window)
canvas.create_image(0, 0, anchor=ttk.NW, image=image)
canvas.pack(fill="both", expand=True)

# Label in main window
title_label = ttk.Label(
    master=window,
    text="Graphical representation of scan conversion algorithms",
    font="Calibri 24 bold",
)
title_label.place(x=300, y=50)

# subtitle
sub_title = ttk.Label(
    master=window, text="Scan conversion line algorithms", font="Calibri 18 bold"
)
sub_title.place(x=65, y=150)

sub_title1 = ttk.Label(
    master=window, text="Scan conversion circle algorithms", font="Calibri 18 bold"
)
sub_title1.place(x=1050, y=150)

sub_title2 = ttk.Label(master=window, text="Take break", font="Calibri 18 bold")
sub_title2.place(x=650, y=300)

# buttons in matin window
button = ttk.Button(
    master=window,
    text="Refresh",
    cursor="circle",
    command= refresh,
    style="outline.primary",
)
button.place(x=35, y=35)

button1 = ttk.Button(
    master=window,
    text="Bresenham circle ",
    cursor="circle",
    command=bresenham,
    style="outline.primary",
)
button1.place(x=1290, y=200)

button2 = ttk.Button(
    master=window,
    text="DDA Line",
    cursor="circle",
    command=dda,
    style="outline.primary",
)
button2.place(x=100, y=200)

button3 = ttk.Button(
    master=window,
    text="Bresenham ",
    cursor="circle",
    command=bresenhamLine,
    style="outline.primary",
)
button3.place(x=194, y=200)

button4 = ttk.Button(
    master=window,
    text="Mid point line ",
    cursor="circle",
    command=midLine,
    style="outline.primary",
)
button4.place(x=300, y=200)

button5 = ttk.Button(
    master=window,
    text="Snake Game ",
    cursor="circle",
    command=snake,
    style="outline.primary",
)
button5.place(x=670, y=340)

button5 = ttk.Button(
    master=window,
    text="Mid point circle",
    cursor="circle",
    command=mid,
    style="outline.primary",
)
button5.place(x=1120, y=200)

window.mainloop()
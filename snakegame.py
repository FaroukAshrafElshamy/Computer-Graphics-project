#                   بسم الله الرحمن الرحيم
#          صلو على نبينا محمد صلى الله عليه و سلم

##############--->>>>>       Mohamed Mostafa Mohamed Abdelhamed     <<<<<---##############
##############--->>>>>          Farouk Ashraf Farouk Elshamy        <<<<<---##############
##############--->>>>>           Omar Mohamed Ahmed Shetewy         <<<<<---##############

from random import randint, choice
from time import sleep
from turtle import *


def snake():
    global health, score

    def Up():
        if head.direction != "Down":
            head.direction = "Up"
            head.setheading(90)

    def Down():
        if head.direction != "Up":
            head.direction = "Down"
            head.setheading(270)

    def Left():
        if head.direction != "Right":
            head.direction = "Left"
            head.setheading(180)

    def Right():
        if head.direction != "Left":
            head.direction = "Right"
            head.setheading(0)

    def move():
        if head.direction == "Up":
            y = head.ycor()
            head.sety(y + 20)

        if head.direction == "Down":
            y = head.ycor()
            head.sety(y - 20)

        if head.direction == "Left":
            x = head.xcor()
            head.setx(x - 20)

        if head.direction == "Right":
            x = head.xcor()
            head.setx(x + 20)

    def Print_Score():
        scores.clear()
        scores.write(
            f"Score: {score}  High Score: {high_score}  Health: {health}",
            align="center",
            font=("Arial", 20, "bold"),
        )

    def Hide_segment():
        global score, delay, health
        for segment in Containers:
            segment.hideturtle()
        Containers.clear()
        health -= 1
        score = 0
        delay = 0.1

        Print_Score()

    def rand_food():
        food.shape(choice(["square", "circle", "turtle", "triangle"]))
        food.color(choice(["red", "#DFFF00", "#31FF00", "#FF00FA", "#04E7FF"]))

    delay = 0.1
    score = 0
    high_score = 0
    health = 3
    x = randint(-500, 500)
    y = randint(-340, 300)

    # Set up the screen
    wn = Screen()
    wn.title("Snake Game")
    wn.bgpic("img2.png")
    wn.setup(1200, 850)
    wn.tracer(0)

    # Set up the border
    outline = Turtle()
    outline.hideturtle()
    outline.up()
    outline.setpos(-540, -380)
    outline.pd()
    outline.color("#4CA9DE", "#084C73")
    outline.begin_fill()
    for i in range(4):
        outline.pensize(5)
        if i % 2 == 0:
            outline.fd(1080)
        else:
            outline.fd(720)
        outline.lt(90)
    outline.end_fill()

    wn.listen()
    wn.onkey(Up, "Up")
    wn.onkey(Down, "Down")
    wn.onkey(Left, "Left")
    wn.onkey(Right, "Right")

    # Snake head
    head = Turtle()
    head.speed(0)
    head.shape("triangle")
    head.color("#092E4A")
    head.penup()
    head.home()
    head.shapesize(1.4)
    head.direction = "Stop"

    # Snake food
    food = Turtle()
    food.speed(0)
    rand_food()
    food.penup()
    food.goto(x, y)

    # Score display
    scores = Turtle()
    scores.speed(0)
    scores.color("#10B8DA")
    scores.penup()
    scores.hideturtle()
    scores.goto(0, 370)
    scores.write(
        f"Score: 0  High Score: 0  Health: {health}",
        align="center",
        font=("Arial", 20, "bold"),
    )

    # Snake body
    Containers = []

    while True:
        wn.update()
        # Check for a collision with the border
        if (
            head.xcor() > 520
            or head.xcor() < -520
            or head.ycor() > 320
            or head.ycor() < -360
        ):
            if health == 1:
                Print_Score()
                break
            sleep(1)
            head.home()
            head.direction = "Stop"
            rand_food()
            Hide_segment()

        # Check for a collision with the food
        if head.distance(food) < 20:
            x = randint(-500, 500)
            y = randint(-340, 300)
            food.goto(x, y)
            rand_food()

            # Add a container
            body = Turtle()
            body.speed(0)
            body.shape("square")
            body.color("#4CA9DE")
            body.penup()
            Containers.append(body)

            # Shorten the delay
            delay -= 0.002
            score += 10
            if score > high_score:
                high_score = score
            Print_Score()

        # How the body follows the head
        for index in range(len(Containers) - 1, 0, -1):
            x = Containers[index - 1].xcor()
            y = Containers[index - 1].ycor()
            Containers[index].goto(x, y)

        if len(Containers) > 0:
            x = head.xcor()
            y = head.ycor()
            Containers[0].goto(x, y)

        move()

        # Check for a collision with the snake's own body
        for segment in Containers:
            if segment.distance(head) < 20:
                sleep(1)
                head.home()
                head.direction = "Stop"

                Hide_segment()

        sleep(delay)

    # Game Over
    over = Turtle()
    over.hideturtle()
    over.write("Game Over", align="center", font=("arial", 50, "bold"))
    over.up()
    over.goto(0, -80)
    over.pd()
    over.write(
        "Made with love by: Farouk Ashraf , Mohamed Mostafa and Omar Shetewy❤️",
        align="center",
        font=("arial", 20, "bold"),
    )

    wn.mainloop()
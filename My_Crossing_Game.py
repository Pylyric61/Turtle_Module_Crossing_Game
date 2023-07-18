from turtle import Turtle, Screen
import random
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("white")

writer = Turtle()
writer.hideturtle()
line = Turtle()

score = 0
time_end = 60

class Display:

    def __init__(self):
        self.player = Turtle()
        self.scoreboard = Turtle()
        self.scoreboard.hideturtle()
        self.scoreboard.penup()
        screen.tracer(2, 1)
        self.l()
        self.colormodule = ["black", "green", "yellow", "blue"]
        self.game_on = True
        self.writer = writer
        self.scoreboard.goto(-230, 250)
        self.random_blocks()
        self.timer = Turtle()
        self.timer.hideturtle()
        self.timer.penup()
        self.timer.goto(200, 250)

    def l(self):
        line.hideturtle()
        var = -60
        mylist = []
        for i in range(6):
            line.pencolor("black")
            line.penup()
            line.goto(320, var)
            var += 40
            a = line.clone()
            mylist.append(a)

        for i in mylist:
            for x in range(35):
                i.speed(5)
                i.pendown()
                i.setheading(180)
                i.forward(10)
                i.penup()
                i.forward(10)

    def gameloop(self):
        screen.clear()
        Display()

    def motion(self):
        global score
        global time_end
        self.player.forward(30)
        if self.player.ycor() > 220 or time_end == 0:
            score += 1
            self.gameloop()

    def random_blocks(self):
        global score
        self.player.hideturtle()
        self.player.shape("turtle")
        self.player.color("red")
        self.player.speed(5)

        self.player.setheading(90)
        self.player.hideturtle()
        self.player.penup()
        self.player.goto(0, -280)
        self.player.speed(5)
        self.player.showturtle()
        block = Turtle()
        block.hideturtle()
        block.shape("turtle")
        block.shapesize(1, 1)
        block.penup()
        block.hideturtle()
        block.color("black")
        block.setheading(180)
        block.hideturtle()
        screen.onkey(self.motion, "Up")
        screen.listen()
        movingobjects1 = []
        movingobjects2 = []
        movingobjects3 = []
        movingobjects4 = []

        for i in range(5):
            a = block.clone()
            b = random.choice([120, 80])
            a.goto(400, b)
            a.showturtle()
            a.color("yellow")
            movingobjects1.append(a)

        for i in range(5):
            a = block.clone()
            b = random.choice([40, 80])
            a.goto(400, b)
            a.showturtle()
            a.color("black")
            movingobjects2.append(a)

        for i in range(5):
            a = block.clone()
            b = random.choice([0, 40])
            a.goto(400, b)
            a.showturtle()
            a.color("blue")
            movingobjects3.append(a)

        for i in range(5):
            a = block.clone()
            b = random.choice([-40, 0])
            a.goto(400, b)
            a.showturtle()
            a.color("yellow")
            movingobjects4.append(a)

        sayar = 0
        obj = [movingobjects1, movingobjects2, movingobjects3, movingobjects4]

        while self.game_on:
            self.scoreboard.write(f"SCORE : {score}", move=False, font=("Arial", 20, "normal"))
            for x in obj:
                for i in range(0, 5):
                    x[i].color(random.choice(self.colormodule))
                    t = random.choice([120, 80])
                    if x[i].ycor() == t:
                        break
                    x[i].forward(10)
                    if 20 > self.player.distance(x[i]) > 5:
                        self.writer.hideturtle()
                        self.writer.penup()
                        self.writer.goto(-60, 250)
                        self.writer.write("GAME OVER", move=False, font=("Arial", 18, "normal"))
                        self.game_on = False
                        time.sleep(1)
                        self.writer.clear()
                        self.gameloop()
                    if x[i].xcor() < -300:
                        x[i].goto(400, x[i].ycor())
                screen.update()

                for i in range(0, 5):
                    x[i].forward(10)
                    t = random.choice([40, 0, -40])
                    if x[i].ycor() == t:
                        break
                    if 20 > self.player.distance(x[i]) > 5:
                        self.writer.hideturtle()
                        self.writer.penup()
                        self.writer.goto(-60, 250)
                        self.writer.write("GAME OVER", move=False, font=("Arial", 18, "normal"))
                        self.game_on = False
                        time.sleep(1)
                        self.writer.clear()
                        self.gameloop()
                    if x[i].xcor() < -300:
                        x[i].goto(400, x[i].ycor())
                screen.update()
                for i in range(0, 5):
                    t = random.choice([40, 0, -40, 120, 80])
                    if x[i].ycor() == t:
                        break
                    x[i].forward(25)
                    if x[i].xcor() == 0:
                        pass
                    if x[i].xcor() < -300:
                        x[i].goto(400, x[i].ycor())
                screen.update()
            sayar += 1
            if sayar > 120:
                self.game_on = False
                self.gameloop()
        screen.exitonclick()

Display()


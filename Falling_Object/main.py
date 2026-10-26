from turtle import Screen, Turtle
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
PLAYER_STEP = 20

screen = Screen()
screen.bgcolor("black")
screen.title("My falling object game")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)


class Player:
    def __init__(self):
        self.p = Turtle()
        self.p.shape("square")
        self.p.color("red")
        self.p.shapesize(stretch_wid=1, stretch_len=3)
        self.p.penup()
        self.p.goto(0, -280)
        self.p.speed(0)

    def moving_left(self):
        if self.p.xcor() > -250:
            self.p.setx(self.p.xcor() - PLAYER_STEP)

    def moving_right(self):
        if self.p.xcor() < 250:
            self.p.setx(self.p.xcor() + PLAYER_STEP)


class Star:
    def __init__(self):
        self.s = Turtle()
        self.s.shape("circle")
        self.s.color("blue")
        self.s.penup()
        self.reset()

    def reset(self):
        self.s.goto(random.randint(-230, 230), 280)
        self.fall_speed = random.randint(3, 7)

    def fall(self):
        self.s.sety(self.s.ycor() - self.fall_speed)
        if self.s.ycor() < -320:
            return True
        return False


star = Star()
player = Player()

screen.listen()
screen.onkey(player.moving_left, "Left")
screen.onkey(player.moving_right, "Right")

score = 0
score_turtle = Turtle()
score_turtle.hideturtle()
score_turtle.color("white")
score_turtle.penup()
score_turtle.goto(0, 260)
score_turtle.write(f"Score: {score}", align="center", font=("Arial", 24, "bold"))

game_running = True


def game_over():
    global game_running
    game_running = False
    score_turtle.goto(0, 0)
    score_turtle.write("GAME OVER", align="center", font=("Arial", 30, "bold"))
    screen.update()
    screen.onclick(lambda x, y: screen.bye())


def game_loop():
    global score
    if not game_running:
        return

    missed = star.fall()
    if player.p.distance(star.s) < 30:
        star.reset()
        score += 1
        score_turtle.clear()
        score_turtle.goto(0, 260)
        score_turtle.write(
            f"Score: {score}", align="center", font=("Arial", 24, "bold")
        )
    elif missed:
        game_over()

    screen.update()
    if game_running:
        screen.ontimer(game_loop, 20)


game_loop()
screen.mainloop()

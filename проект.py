import turtle


borders ={
    "maxX": 390,
    "minX": -390,
    "maxY": 290,
    "minY": -290
}

wn = turtle.Screen()
wn.title("Пинг-понг")
wn.bgcolor("black")
wn.setup(width=800, height=800)
wn.tracer(0)

left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=6, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350,0)

right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=6, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350,0)


ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = -0.2




def left_paddle_up():
    y = left_paddle.ycor()
    if y < 250:
        y+= 20
        left_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    if y < -240:
        y -= 20
        left_paddle.sety(y)


def right_paddle_up():
    y = right_paddle.ycor()
    if y < 250:
        y += 20
        right_paddle.sety(y)


def right_paddle_down():
    y = right_paddle.ycor()
    if y < -240:
        y -= 20
        right_paddle.sety(y)

wn.listen()
wn.onkeypress(left_paddle_up, "w")
wn.onkeypress(left_paddle_down, "s")

wn.onkeypress(right_paddle_up, "Up")
wn.onkeypress(right_paddle_down, "Down")


while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > borders["maxY"]:
        ball.sety(borders["maxY"])
        ball.dy *= -1

    if ball.ycor() < borders["minY"]:
        ball.sety(borders["minY"])
        ball.dy *= -1

    if ( ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() > right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1








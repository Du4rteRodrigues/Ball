import turtle

game = True
wn = turtle.Screen()
ball = turtle.Turtle()
paddle = turtle.Turtle()
pen = turtle.Turtle()
show_score = turtle.Turtle()
score = 0
reset = 0

#=====================================================================================================

# Window
window =[
    wn.title("Ball"),
    wn.bgcolor("black"),
    wn.setup(width=800,height=600),
    wn.tracer(0)
]


# Pen
message = [
    pen.speed(0),
    pen.color("White"),
    pen.penup(),
    pen.hideturtle(),
    pen.goto(0,40)
]


# Score
ss = [
    show_score.speed(0),
    show_score.color("White"),
    show_score.penup(),
    show_score.hideturtle(),
    show_score.goto(0,100),
    show_score.write("Score: 0", align="center", font = ("Courier", 24, "normal"))
]


# Enemies
enemies = []
for e in range(21):
    enemies.append(turtle.Turtle())
    
for enemy in enemies:
    enemy.speed(0)
    enemy.shape("square")
    for i in range(len(enemies)):
        if enemies[i]:
            if i <= 6:
                enemies[i].color("Red")
                continue

            if i <= 13:
                enemies[i].color("Yellow")
                continue

            if i <= 20:
                enemies[i].color("Green")
                continue
    enemy.shapesize(stretch_wid=0.5, stretch_len=5)
    enemy.penup()


# Enemy positions
enemy_list = [
    enemies[0].goto(-330,290),
    enemies[1].goto(-220,290),
    enemies[2].goto(-110,290),
    enemies[3].goto(0,290),
    enemies[4].goto(110,290),
    enemies[5].goto(220,290),
    enemies[6].goto(330,290),

    enemies[7].goto(-330,270),
    enemies[8].goto(-220,270),
    enemies[9].goto(-110,270),
    enemies[10].goto(0,270),
    enemies[11].goto(110,270),
    enemies[12].goto(220,270),
    enemies[13].goto(330,270),

    enemies[14].goto(-330,250),
    enemies[15].goto(-220,250),
    enemies[16].goto(-110,250),
    enemies[17].goto(0,250),
    enemies[18].goto(110,250),
    enemies[19].goto(220,250),
    enemies[20].goto(330,250)
]


# Ball 
ball_stats = [
    ball.speed(0),
    ball.shape("circle"),
    ball.color("White"),
    ball.penup()
    ]
ball.dx = 0.5  
ball.dy = 0.5


# Paddle
paddle_stats = [
        paddle.speed(0),
        paddle.shape("square"),
        paddle.color("White"),
        paddle.shapesize(stretch_wid=1, stretch_len=7),
        paddle.penup(),
        paddle.setx(0),
        paddle.sety(-255)

]

# Paddle movement
def paddle_left():
    x = paddle.xcor()
    x += 20
    paddle.setx(x)

def paddle_right():
    x = paddle.xcor()
    x -= 20
    paddle.setx(x)

    
# Keybindings
window_stats = [
    wn.listen(),
    wn.onkeypress(paddle_right, "a"),
    wn.onkeypress(paddle_left, "d"),
    wn.onkeypress(paddle_right,"Left"),
    wn.onkeypress(paddle_left, "Right")
]

#==========================================================================================================

# Main game loop
while game == True:
    wn.update()

    # Movement of ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

# Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # Paddle reaching corners
    if paddle.xcor() > 330:
        paddle.goto(330,-255)

    if paddle.xcor() < -330:
        paddle.goto(-330,-255)
    
    # Restart
    if ball.ycor() < -290:
        show_score.clear()
        show_score.write(f"Score: {score}", align="center", font = ("Courier", 24, "normal"))
        pen.write(f"YOU LOST :(", align="center", font = ("Courier", 40, "normal"))
        ball.dx = 0  
        ball.dy = 0
        ball.goto(0,0)
        paddle.goto(0,-255)

    # Ball touches borders
    if ball.xcor() > 380:
        ball.setx(380)
        ball.dx *= -1

    if ball.xcor() < -380:
        ball.setx(-380)
        ball.dx*= -1


    # Paddle and ball collisions 
    if (ball.ycor() < -245 and ball.ycor() > -265) and (ball.xcor() < paddle.xcor() + 70 and ball.xcor() > paddle.xcor() -70):
        ball.dy *= -1


    # Ball and enemy collisons
    for i in range(len(enemies)):
        if enemies[i]:
            if i <= 6:
                if (ball.ycor() < enemies[i].ycor() +10 and ball.ycor() > enemies[i].ycor()-10) and (ball.xcor() < enemies[i].xcor() + 40 and ball.xcor() > enemies[i].xcor() -40):
                    ball.dy *= -1
                    enemies[i].hideturtle()
                    enemies[i] = None
                    score += 10
                    show_score.clear()
                    show_score.write(f"Score: {score}", align="center", font = ("Courier", 24, "normal"))
                    break
                
            if i <= 13:
                if (ball.ycor() < enemies[i].ycor() +10 and ball.ycor() > enemies[i].ycor()-10) and (ball.xcor() < enemies[i].xcor() + 40 and ball.xcor() > enemies[i].xcor() -40):
                    ball.dy *= -1
                    enemies[i].hideturtle()
                    enemies[i] = None
                    score += 10
                    show_score.clear()
                    show_score.write(f"Score: {score}", align="center", font = ("Courier", 24, "normal"))
                    break

            if i <= 20:
                if (ball.ycor() < enemies[i].ycor() +10 and ball.ycor() > enemies[i].ycor()-10) and (ball.xcor() < enemies[i].xcor() + 40 and ball.xcor() > enemies[i].xcor() -40):
                    ball.dy *= -1
                    enemies[i].hideturtle()
                    enemies[i] = None
                    score += 10
                    show_score.clear()
                    show_score.write(f"Score: {score}", align="center", font = ("Courier", 24, "normal"))
                    break

# End of game
    for i in range(len(enemies)):
        if len(enemies) == 0:
            ball.dx = 0 
            ball.dy = 0
            ball.goto(0,0)
            paddle.goto(0,-255)
            pen.write("YOU WON!", align="center", font = ("Courier", 24, "normal"))
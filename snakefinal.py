from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
score = 0
snake_color = 'green'
food_color = 'red'

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    global score, snake_color, food_color
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        goto(0, 0)
        write("Game Over", align="center", font=("Arial", 24, "normal"))
        return

    snake.append(head)

    if head == food:
        score += 1
        print('Score:', score)
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        # Change colors randomly
        snake_color = (randrange(256), randrange(256), randrange(256))
        food_color = (randrange(256), randrange(256), randrange(256))
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100 - min(score * 2, 90))

def draw_boundaries():
    "Draw the boundaries of the game area."
    penup()
    goto(-200, -200)
    pendown()
    for _ in range(4):
        forward(390)
        left(90)
    penup()

def setup():
    "Set up the game."
    hideturtle()
    tracer(False)
    listen()
    onkey(lambda: change(10, 0), 'Right')
    onkey(lambda: change(-10, 0), 'Left')
    onkey(lambda: change(0, 10), 'Up')
    onkey(lambda: change(0, -10), 'Down')
    draw_boundaries()
    move()
    done()

# Set up the screen
colormode(255)
setup()

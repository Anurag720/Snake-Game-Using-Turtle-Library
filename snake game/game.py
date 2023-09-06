import turtle # for making graphics 
import random # for generating random numbers 
import time   # to provide delay and speed control

# creating screen
screen = turtle.Screen() # this function used to create game screen
screen.title("SNAKE GAME")
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("#1d1d1d")

# creating border
border = turtle.Turtle()  # Create a turtle object for the border
border.speed(5) #speed of a turtle how fast it moves while drawing
border.pensize(4)  # Width of our border
border.penup() # used to tip up or pen up the turtle so it cannot draw 
border.goto(-310, 250) 
border.pendown()
border.color("red")
border.forward(600)
border.right(90)
border.forward(500)
border.right(90)
border.forward(600)
border.right(90)
border.forward(500)
border.right(90)
border.penup()
border.hideturtle()

# score
score = 0
delay = 0.1

# snake
snake = turtle.Turtle() # creating object
snake.speed(0)
snake.shape("square")
snake.color("blue")
snake.penup()
snake.goto(0, 0) #intial position means snake start from center
snake.direction = 'stop' # snake not move intially
# food
fruit = turtle.Turtle()
fruit.speed(0) # very fast without any animaton
fruit.shape("square")
fruit.color("white")
fruit.penup()
fruit.goto(30, 30)

# snake size
old_fruit = []

# scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("SCORE :", align="center", font=("Courier", 24, "bold"))


# movement
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"


def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"


def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"


def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"


def snake_mov():
    if snake.direction == "up":
        y = snake.ycor() # get current cordinate of snake
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)


# keyboard control
screen.listen()
screen.onkeypress(snake_go_up, "Up") # when up key press called up function
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

# main loop
while True:
    screen.update()

    # snake and fruit eating
    if snake.distance(fruit) < 20: # means snake has eaten
        x = random.randint(-290, 270) # random food generation
        y = random.randint(-248, 240)
        fruit.goto(x, y)
        scoring.clear()
        score += 1
        scoring.write("SCORE : {}".format(score), align="center", font=("Courier", 24, "bold"))
        delay -= 0.001 # used to increase game speed

        # creating new fruit
        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape("square")
        new_fruit.color('red')
        new_fruit.penup()
        old_fruit.append(new_fruit)

    # adding ball to snake
    for index in range(len(old_fruit) - 1, 0, -1):
        a = old_fruit[index - 1].xcor()
        b = old_fruit[index - 1].ycor()
        old_fruit[index].goto(a, b)
    if len(old_fruit) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_fruit[0].goto(a, b)
    snake_mov()

    # snake border collision
    if snake.xcor() > 288 or snake.xcor() < -300 or snake.ycor() > 248 or snake.ycor() < -248:
        time.sleep(1)
        screen.clear()
        screen.bgcolor("turquoise")
        scoring.goto(0, 0)
        scoring.write("GAME OVER\nYour Score is {}".format(score), align="center", font=("Courier", 24, "bold"))

    # snake collision
    for food in old_fruit:
        if food.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("turquoise")
            scoring.goto(0, 0)
            scoring.write("GAME OVER\nYour Score is {}".format(score), align="center", font=("Courier", 24, "bold"))

    time.sleep(delay)

# Exit on click
turtle.done()

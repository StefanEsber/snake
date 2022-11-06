from snake import Snake
from turtle import Screen
from food import Food
import time
from score import Score

# Screen size and visual
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
# Object imported from each class

snake = Snake()
food = Food()
score = Score()

# Snake movement on screen
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        score.snake_ate_food()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.game_over()
        game_over = True

    # Detect collision with tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            game_over = True
            score.game_over()

screen.exitonclick()

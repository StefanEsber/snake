from snake import Snake
from turtle import Screen
from food import Food
import time
from score import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
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

    if snake.head.distance(food) < 15:
        snake.create_snake()
        food.refresh()
        score.snake_ate_food()

screen.exitonclick()

import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

# screenの設定
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("🐍Snake game")
screen.tracer(0)

# snakeの移動
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # スネークとフードの接触
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # 壁に接触
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280) or (snake.head.ycor() > 280 or snake.head.ycor() < -280):
        scoreboard.reset()
        snake.reset()

    # 自身に接触
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

# 終了
screen.exitonclick()

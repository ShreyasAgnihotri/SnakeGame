from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(height = 600, width = 600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

snake = Snake() 
food = Food()
score = Scoreboard()
screen.listen()   
screen.onkey(snake.up,"Up")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.down,"Down")
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        score.reset()
        snake.reset()
    for segments in snake.segments[1:]:
        if snake.segments[0].distance(segments) < 10:
            score.reset()
            snake.reset()



screen.exitonclick()
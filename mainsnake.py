import random
from turtle import Turtle,Screen
from snakeclass import Snake
from snakefood import Food
from snakescore import Scoreb
import time

my_screen=Screen()
my_screen.setup(width=600,height=600)
my_screen.tracer(0)
my_screen.bgcolor("black")
my_screen.title("my snake game")

snake=Snake()
food=Food()
scoreb=Scoreb()
my_screen.listen()
my_screen.onkey(snake.up,"Up")
my_screen.onkey(snake.down,"Down")
my_screen.onkey(snake.left,"Left")
my_screen.onkey(snake.right,"Right")

game_is_on=True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<15:
       food.refresh()
       snake.extend()
       scoreb.increase()
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        scoreb.reset()
        snake.reset()
        # game_is_on=False
    for segment in snake.segments[1:]:
    #    if segment==snake.head:
    #       pass
    #    if snake.head.distance(segment)<10:
    #       scoreb.game_over()
    #       game_is_on=False
       if snake.head.distance(segment)<10:
           scoreb.reset()
           snake.reset()
        #    game_is_on=False
         

        

        
        


        
        
        
   






my_screen.exitonclick()
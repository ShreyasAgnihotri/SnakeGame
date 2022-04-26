from turtle import Turtle
POSITIONS = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
    def create_snake(self):
        for i in POSITIONS:
            self.add_segment(i)
    def add_segment(self,position):
        snake = Turtle(shape = "square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)
    def reset(self):
        for i in self.segments:
            i.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            x_pos = self.segments[i-1].xcor()
            y_pos = self.segments[i-1].ycor()
            self.segments[i].goto(x_pos,y_pos)
        self.segments[0].forward(20) 
    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
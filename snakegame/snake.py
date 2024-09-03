from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.grow_snake(position)

    def grow_snake(self, position):  # Added position parameter
        t = Turtle()
        t.shape("square")
        t.color("white")
        t.speed(3)
        t.penup()  # Prevent drawing lines between segments
        t.goto(position)  # Positioning each segment at the correct coordinate
        self.snake_body.append(t)

    def extend_snake(self):
        self.grow_snake(self.snake_body[-1].position())

    def move(self):
        for _ in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[_ - 1].xcor()
            new_y = self.snake_body[_ - 1].ycor()
            self.snake_body[_].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

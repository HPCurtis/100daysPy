from turtle import Turtle

class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)
        self.x_move = 10
        self.y_move = 10
        # Stating timer speed specification
        # which sets the ball speed behaviour.
        self.movement_speed = .1
    
    def move(self):
        
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        # Change the balss direction of travel in y coordinate
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        # When a change in x direction which fundmentally
        # is a succesful paddle strike the time delay 
        # is reduced speeding up the ball
        self.movement_speed *= .95

    def reset_pos(self):
        self.goto(0,0)
        self.movement_speed = .1
        self.bounce_x()
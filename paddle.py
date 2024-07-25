from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1, outline=20)
        self.goto(x_cor, y_cor)

    def up(self):
        if self.ycor()<230:
            y_cor=self.ycor()+20
            self.goto(self.xcor(),y_cor)

    def down(self):
        if self.ycor() > -230:
            y_cor = self.ycor() - 20
            self.goto(self.xcor(), y_cor)

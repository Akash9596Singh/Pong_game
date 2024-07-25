from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.score = 0
        self.penup()
        self.hideturtle()
    def change_score(self):
        self.score += 1


score=Score()
print(score)
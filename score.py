from turtle import Turtle,Screen
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 350)
        self.score = 0
        self.color('black')
        self.update_board()
        self.hideturtle()
    def update_board(self):

        self.write(f'score:{self.score}', align='center', font=('Arial', 20, 'bold'))
    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_board()
    def game_over(self):
        self.screen.bgcolor('red')
        self.goto(0, 0)
        self.hideturtle()
        self.write(f'     game over\nyour final score is {self.score}', align='center', font=('Arial', 20, 'bold'))
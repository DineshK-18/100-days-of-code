from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 22, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'score= {self.score}', move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER!', move=False, align=ALIGNMENT, font=FONT)


    def update_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()



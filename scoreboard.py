from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_count = 0
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 265)
        self.write(f"Score: {self.score_count} High Score: {self.high_score}", True, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score_count += 1
        self.update_score()

    def reset(self):
        if self.score_count > self.high_score:
            self.high_score = self.score_count
            with open("data.txt", "w") as file:
                file.write(str(self.score_count))
        self.score_count = 0
        self.update_score()

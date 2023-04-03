from turtle import Turtle

FONT = ("courier", 8, "normal")


class ShowState(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def update_state(self, state_name, state_x, state_y):
        self.goto(state_x, state_y)
        self.write(state_name, align="center", font=FONT)

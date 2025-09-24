from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which color do you want to choose? Enter a color:")
print(user_bet)

racers = []
y_pos = [80, 40, 0, -40, -80, -120]
colors = ["red", "orange", "blue", "green", "yellow", "purple"]

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[i])
    racers.append(new_turtle)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for racer in racers:
        random_dist = randint(0, 10)
        racer.forward(random_dist)

        if racer.xcor() > 230:
            is_race_on = False
            winning_color = racer.pencolor()
            if winning_color.lower() == user_bet.lower():
                print(f"You've WON! Your turtle {winning_color} has won the race!")
            else:
                print(f"You've LOST! The turtle {winning_color} has won the race!")

screen.exitonclick()

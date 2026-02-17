import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv('50_states.csv')
states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_text = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                   prompt="What's another state's name?").title()
    if answer_text == 'Exit':
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_text in states and answer_text not in guessed_states:
        guessed_states.append(answer_text)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_text]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_text)


turtle.mainloop()



import pandas
from turtle import Screen
from my_turtle import WritingTurtle

screen = Screen()
screen.title("US states game")
image = 'blank_states_img.gif'
screen.bgpic(image)
score = 0
my_turtle = WritingTurtle()
guessed_states = []

data = pandas.read_csv("50_states.csv")
data_list = data.state.to_list()


while score < 50:
    answer_text = screen.textinput(title=f"Guess the state {score}/50", prompt="What's another states game?").title() ## ignore
    if answer_text == "Exit":
        missing_states = [state for state in data_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    elif answer_text in data_list:
        new_cor = data[data.state == answer_text]
        score += 1
        guessed_states.append(answer_text)
        my_turtle.write_state(answer_text, int(new_cor.x), int(new_cor.y))


screen.exitonclick()
import turtle

import pandas

import state_write
from state_write import ShowState
from search_state import SearchState

# Initialize game elements
screen = turtle.Screen()
screen.title("US States Game")
show_state = ShowState()
search_state = SearchState()
guessed_states = []
guessed_states_num = 0
game_is_on = True

# Get image for background
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Infinite Loop
while game_is_on:
    # Create prompt
    answer_state = screen.textinput(title=f"{guessed_states_num}/50 states guessed",
                                    prompt="What's another state's name?")
    answer_state = answer_state.title()

    # Exit formula which exports .csv with missing states
    if answer_state == "Exit":
        not_guessed_states = search_state.not_guessed_states(guessed_states)
        not_guessed_df = pandas.DataFrame(data=not_guessed_states, columns=["Not guessed States"])
        not_guessed_df.to_csv("missing_states.csv")
        break

    # Check if answer is a state
    # Also check if not already guessed
    if answer_state not in guessed_states:
        is_state_correct = search_state.check_state(answer_state)
        if is_state_correct:
            state_cor = search_state.get_state_cor(answer_state)
            show_state.update_state(state_name=state_cor[0], state_x=state_cor[1], state_y=state_cor[2])
            guessed_states.append(state_cor[0])
            guessed_states_num += 1

    if guessed_states_num == 50:
        game_is_on = False

# Exit on click
screen.exitonclick()

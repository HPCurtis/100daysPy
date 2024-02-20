# Import libraries
import pandas as pd 
import turtle

# Set local file paths to variables as global constants
STATES = "50_states.csv"
IMAGE =  "blank_states_img.gif"
GUESSES = 50
 
def main():
    data = read_states_csv(STATES)
    data_c = read_states_csv(STATES) 
    
    gen_screen(IMAGE, data, data_c)

def gen_screen(IMAGE, data, data_c):
    # Create screen object with .Screen Class
    screen = turtle.Screen()
    # Give the screen a title.
    screen.title("U.S. states game")

    # Add the gif to the screen objects shape.
    screen.addshape(IMAGE)

    # When image added to the screen it cna be presneted by turtle.shape()
    turtle.shape(IMAGE)

    correct_count = 0
    guessed_states = []

    while len(guessed_states) < GUESSES:
        # output text input scrren to users.
        answer_state = screen.textinput(title= f"{correct_count}/50 States Correct", prompt = "Whats the name of a U.S. state")

        # use.title() method so that eben is inputted clower case
        answer_state = answer_state.lower().title()

        # Know check if answers is U.S. state
        if answer_state == "Exit":
            break
        if answer_state in data["state"].values:
            correct_count += 1
            x, y = get_xy(answer_state, data)
            
            data = drop_state(answer_state, data)
            
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(x, y) 
            t.pendown()

            # Write text
            t.write(answer_state)
            
            # Hide the turtle
            # Keep the window open
        
        else:
            pass

        guessed_states.append(answer_state)

    # Convert guessed states to get all unique responses and remove repeitions
    guessed_states = set(guessed_states)
    states_to_learn_csv(data_c.state, guessed_states)

    screen.exitonclick()

def get_xy(answer, data):
   
        # Boolean idnex
        row_select = data['state'] == answer

        # Use boolean indexing to filter columns based on the condition
        filtered_columns = data.loc[row_select, :]
        return (filtered_columns['x'].values[0], filtered_columns['y'].values[0])

def drop_state(answer, data):
    # Define the condition to drop rows
    condition = data['state'] == answer

    # Use boolean indexing to select rows that don't match the condition
    data = data[~condition]
    return data


def read_states_csv(STATES):
    return pd.read_csv(STATES)

def states_to_learn_csv(states, guesses):
    states = set(states)
    diff = states.difference(guesses)
    
    df = pd.DataFrame(diff, columns=['states_to_learn'])
    df.to_csv('output.csv', index=False)

if __name__ == "__main__":
    main()

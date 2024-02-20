import random
def check_guess(compeititors, screen):
    while True:
        try:
            # Get competitors guess
            guess = screen.textinput(title="Make your bet",prompt="who will win the race")
            # convert string lowercase for is user input control flow.
            guess.lower()
            if guess in compeititors:
                return guess
            else:
                raise ValueError
        except ValueError:
            print("please enter a valid compeitor name")

def move_to_side(t, width, y):
    t.penup()
    t.goto(-width/2 + 10, y)

def move_forward(t_dict, width, guess):

    distance_dict = {
    "harrison": 0,
    "brandon": 0,
    "fraser": 0,
    "ashley": 0
}
    while True:
        key = random.choice(list(t_dict.keys()))
        t_dict[key].forward(10)
        distance_dict[key] += 10

        if distance_dict[key] >= width:
            if guess == key:
                return f"You win. the {key} turtle is the winner"
            else:
                return f"You lose. the {key} turtle is the winner"
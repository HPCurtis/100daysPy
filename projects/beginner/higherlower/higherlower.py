from higherlowerart import logohl, vslogo
from game_data import gdata
from utility import *

count = 0

while True:
    fc_a, fc_b, user_input, result = main_call(count)

    if result:
        count += 1
        print(f"That's correct your score is. {count}")
    else:
        clear_screen()
        print(logohl())
        print(f"Sorry that's wrong. Your final score is. {count}")
        break

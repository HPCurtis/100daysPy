from tkinter import *
import time
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CANVAS_WIDTH = 200
CANVAS_HEIGHT = 224

# Specify global variables
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00::00")
    label_timer(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_secs)
        label_timer.config(text= "Break", fg = RED)
    elif reps % 2 == 0:
        count_down(short_break_secs)
        label_timer.config(text="Break", fg = PINK)
    else:
        count_down(work_sec)
        label_timer.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro method timer")
window.config(padx=100, pady=50, bg=YELLOW)

label_timer = Label(window, text="Timer", fg=GREEN, bg = YELLOW,  font=(FONT_NAME, 50, "bold"))
label_timer.grid(column=1, row=0)

canvas = Canvas(width= 200, height=224, bg=YELLOW, highlightthickness=0)
tom_image = PhotoImage(file = "tomato.png")

canvas.create_image(int(CANVAS_WIDTH/2), int(CANVAS_HEIGHT/2), image =  tom_image)
timer_text = canvas.create_text(103, 130, text="00:00", fill = "white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

#Create a check mark 
check_mark = Label(fg= GREEN, bg = YELLOW)
check_mark.grid(column=1, row=2)


window.mainloop()
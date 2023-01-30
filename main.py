from tkinter import Tk, Canvas, Label, Button, PhotoImage
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Consolas"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer", fg=GREEN)
    check.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(long_break_secs)
        title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_secs)
        title.config(text="Break", fg=PINK)
    else:
        count_down(work_secs)
        title.config(text="Work", fg=GREEN)
        work_session_count = floor(reps / 2)
        check_str = ""
        for _ in range(work_session_count):
            check_str += "✔️"
        check.config(text=f"{check_str}", font=(FONT_NAME, 22, "bold"), bg=YELLOW, fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_secs = count % 60
    if count_secs < 10:
        count_secs = f"0{count_secs}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_secs}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="icons/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 22, "bold"), fill="white")
canvas.grid(row=1, column=1)

title = Label(text="Timer", font=(FONT_NAME, 34, "bold"), bg=YELLOW, fg=GREEN)
title.grid(row=0, column=1)

start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(row=2, column=2)

check = Label(text="", font=(FONT_NAME, 22, "bold"), bg=YELLOW, fg=GREEN)
check.grid(row=3, column=1)

window.mainloop()

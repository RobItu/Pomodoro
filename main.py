import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN, font=(FONT_NAME, 38, "bold"), bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    checkmark.config(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    global checks
    reps += 1
    if reps == 8:
        count_down(LONG_BREAK_MIN*60)
        timer_label.config(text=" 😭 LONG BREAK TIME 😭 ", fg=GREEN)
        checks = ""
    elif reps%2 == 0 and reps != 0:
        count_down(SHORT_BREAK_MIN*60)
        timer_label.config(text="😘 SHORT BREAK 😘", fg=PINK)
    else:
        count_down(WORK_MIN*60)
        timer_label.config(text="💯😤 WORK TIME 😤💯", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global checks
    counter_min = math.floor(count / 60)
    counter_sec = count % 60
    if counter_sec < 10:
        counter_sec = f"0{counter_sec}"

    canvas.itemconfig(timer_text, text=f"{counter_min}:{counter_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
        checkmark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 38, "bold"), bg=YELLOW)
timer_label.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
checkmark.grid(column=1, row=3)

window.mainloop()

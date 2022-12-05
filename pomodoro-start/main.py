from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 0

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    label_title.config(text="Timer", fg=GREEN)
    label_checkmark.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_start():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        label_title.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label_title.config(text="Break", fg=PINK)
        # label_checkmark.config(text=check)
        count_down(short_break_sec)
    else:
        label_title.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        timer_start()
        mark = ""
        for _ in range(reps // 2):
            mark += "✔"
            label_checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=100, pady=80, bg=YELLOW)
window.title("Pomodoro")

canvas = Canvas(height=250, width=224, bg=YELLOW, highlightthickness=0)
# ------- Create Image ------- #
photo_image = PhotoImage(file="tomato.png")
canvas.create_image(115, 112, image=photo_image)
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(
    115, 130, text="00:00", fill="#fff", font=(FONT_NAME, 30, "bold")
)
# ------- Create Label ------- #
label_title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
label_title.grid(column=1, row=0)

label_checkmark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
label_checkmark.grid(column=1, row=3)

# ------- Create Buttons ------- #
button_start = Button(text="Start", command=timer_start, padx=15, pady=5, border=0)
button_start.grid(column=0, row=2)
button_reset = Button(text="Reset", command=reset_timer, padx=15, pady=5, border=0)
button_reset.grid(column=2, row=2)

window.mainloop()

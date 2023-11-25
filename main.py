from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #

# Color constants for visual elements
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

# Font constant for consistent text styling
FONT_NAME = "Times New Roman"

# Time constants in minutes
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Global variables to keep track of the timer and repetitions
timer = ""
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    # Cancel any ongoing timer
    window.after_cancel(timer)
    # Reset the displayed timer text to "00:00"
    canvas.itemconfig(timer_text, text="25:00")
    header.config(text="Timer")
    tick.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    # Configure timer based on the number of repetitions
    if reps % 8 == 0:
        # Start a long break and update header color
        count_down(LONG_BREAK_MIN * 60)
        header.config(text="Long Break", fg=PINK)
    elif reps % 2 == 0:
        # Start a short break and update header color
        count_down(SHORT_BREAK_MIN * 60)
        header.config(text="Break", fg=RED)
    else:
        # Start a work session and update header color
        count_down(WORK_MIN * 60)
        header.config(text="Work", fg=GREEN)


# ---------------------------- EXIT THE APP COMMAND ------------------------------ #
def exit_app():
    window.destroy()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # Convert total seconds into minutes and seconds
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # Ensure seconds are displayed with leading zero if less than 10
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    # Update the displayed timer text on the canvas
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    # If there are remaining seconds, continue the countdown; otherwise, start a new timer
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        checkmarks = ""
        # add one checkmark for every work session completed
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            checkmarks += "✔"
        tick.config(text=checkmarks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Clock")
window.config(padx=100, pady=50, background=YELLOW, borderwidth=4, relief="groove")

# Canvas setup to display tomato image and timer text
canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 128, text="25:00", font=(FONT_NAME, 20, "bold"), fill="white")
canvas.grid(column=1, row=1)

# Labels for the timer header and completion tick
header = Label(bg=YELLOW, fg=GREEN, text="Timer", font=(FONT_NAME, 34, "bold"))
header.grid(column=1, row=0)

tick = Label(fg=GREEN, font=(FONT_NAME, 24, "bold"))
tick.grid(column=1, row=2)

# Dropdown time selection menu
time_options = [25, 15, 10]

# datatype of menu text
clicked = StringVar()

# Radio buttons timer selection

# Buttons to start and reset the timer and to exit the app
start_button = Button(text="Start", command=start_timer)
start_button.config(font=(FONT_NAME, 14, "bold"), cursor="hand2", activeforeground=GREEN)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.config(font=(FONT_NAME, 14, "bold"), cursor="hand2", activeforeground=GREEN)
reset_button.grid(column=2, row=2)

exit_button = Button(text="Exit", command=exit_app)
exit_button.config(font=(FONT_NAME, 14, "bold"), cursor="hand2", foreground=RED, activeforeground=RED,
                   padx=20, borderwidth=4, relief="ridge")
exit_button.grid(column=1, row=3)
# Start the Tkinter event loop
window.mainloop()

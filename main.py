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
reps = 0
n = 0
text = '✔'
my = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps, n
    n = 0
    reps = 0
    label['text'] = 'Timer'
    lab['text'] = ''
    canvas.itemconfig(timer, text=f'0:00')
    window.after_cancel(my)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start1():
    work = WORK_MIN * 60
    short = SHORT_BREAK_MIN * 60
    long = LONG_BREAK_MIN * 60
    global reps, n, text
    reps += 1
    if reps % 2 == 1:
        label['text'] = 'Working'
        label['fg'] = PINK
        start(work)
    elif reps % 8 == 0:
        label['text'] = 'Long Break'
        start(long)
    elif reps % 2 == 0:
        label['text'] = 'Break'
        start(short)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start(count1):
    global n
    if count1 >= 0:
        min = math.floor(count1 / 60)
        sec = count1 % 60
        if int(sec) < 10:
            sec = f'0{sec}'
        canvas.itemconfig(timer, text=f'{min}:{sec}')
        if count1 > 0:
            global my
            my = window.after(1000, start, count1 - 1)
        else:
            if reps % 2 == 0:
                n += 1
                lab.config(text=text * n)
            start1()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
lab = Label(bg=GREEN, fg=YELLOW)
window.title('Pomodoro Technique')
window.config(padx=40, pady=40, bg=GREEN)
label = Label(text='Timer', font=(FONT_NAME, 25, 'bold'), fg=RED, bg=GREEN)
canvas = Canvas(window, height=300, width=300, bg=GREEN, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(150, 150, image=photo)
timer = canvas.create_text(150, 150, fill='black', font=(FONT_NAME, 25, 'bold'), text='0:00')
button_start = Button(text='START', command=start1, highlightthickness=0)
reset_button = Button(text='RESET', command=reset, highlightthickness=0)
label.grid(column=1, row=0)
lab.grid(column=1, row=2)
button_start.grid(column=0, row=2)
canvas.grid(column=1, row=1)
reset_button.grid(column=2, row=2)
window.mainloop()

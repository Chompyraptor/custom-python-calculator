# T R Hoshino
# 13/09/2022

# ***************************************************
# Python Calculator with GUI (Graphic User Interface)
# ***************************************************

from tkinter import *

def button_press(num):
    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

def equals():
    global equation_text

    try:

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total
        
    except SyntaxError:

        equation_text.set("syntax error")

        equation_text = ""

    except ZeroDivisionError:

        equation_label.set("arithmetic error")

        equation_text = ""

def clear():
    global equation_text

    equation_label.set("")

    equation_text = ""

window = Tk()
window.title("Python Calculator")
window.geometry("500x500")
window.configure(bg="#c9f5ed") # This is coloured a light blue so it is not distracting but makes the buttons easier to see.

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('console', 20), bg="white", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

# The number buttons are not in colour as it would make things overcomplicated.

button1 = Button(frame, text=1, width=9, height=4, font=35, command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, width=9, height=4, font=35, command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, width=9, height=4, font=35, command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, width=9, height=4, font=35, command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, width=9, height=4, font=35, command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, width=9, height=4, font=35, command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, width=9, height=4, font=35, command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, width=9, height=4, font=35, command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, width=9, height=4, font=35, command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, width=9, height=4, font=35, command=lambda: button_press(0))
button0.grid(row=3, column=0)

# The operation and equals buttons are in orange to make them stand out from the other buttons.

plus = Button(frame, bg="#e3a566", text='+', width=9, height=4, font=35, command=lambda: button_press('+'))
plus.grid(row=0, column=4)

minus = Button(frame, bg="#e3a566", text='-', width=9, height=4, font=35, command=lambda: button_press('-'))
minus.grid(row=1, column=4)

multiply = Button(frame, bg="#e3a566", text='x', width=9, height=4, font=35, command=lambda: button_press('*'))
multiply.grid(row=2, column=4)
# This is aimed at third year elementary school students so there is no division button.
equal = Button(frame, bg="#e3a566", text='=', width=9, height=4, font=35, command=equals)
equal.grid(row=3, column=4)

# This button is not coloured as it is the only word button and they should be able to read.
clear = Button(frame, text='clear', width=9, height=4, font=35, command=clear)
clear.grid(row=3, column=2)


window.mainloop()
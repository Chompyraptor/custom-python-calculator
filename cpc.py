# T R Hoshino
# 13/09/2022

# ***************************************************
# Python Calculator with GUI (Graphic User Interface)
# ***************************************************

from tkinter import * # import the tkinter library 

def button_press(num): # defining each button press
    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

def equals(): # this block checks for the button_press(equals)
    global equation_text

    try: # try is used in try...except blocks. It defines a block of code test if it contains any errors.
         # You can define different blocks for different error types, and blocks to execute.

        total = str(eval(equation_text)) # parses the expression arguement and evaluates it as a python expression.

        equation_label.set(total)

        equation_text = total
        
    except SyntaxError: # Check for syntax error

        equation_text.set("syntax error")

        equation_text = ""

    except ZeroDivisionError: # Check for division by zero

        equation_label.set("arithmetic error")

        equation_text = ""

def clear(): # Clears the equation_label for the next calculation
    global equation_text

    equation_label.set("")

    equation_text = ""

# Designing the user interface

window = Tk() # you can use window, root, ... or a descriptive variable of your own
window.title("Python Calculator") # Title in the window bar
window.geometry("500x500") # size of the window dependant on your design
window.configure(bg="#c9f5ed") # window colour dependant on your design

equation_text = "" # starting off with no text in the label

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('console', 20), bg="white", width=24, height=2)
label.pack() # widgets have to be "pack"ed into the window

frame = Frame(window)
frame.pack() # the frame

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

# create operation button

plus = Button(frame, text='+', width=9, height=4, font=35, command=lambda: button_press('+'))
plus.grid(row=0, column=4)

minus = Button(frame, text='-', width=9, height=4, font=35, command=lambda: button_press('-'))
minus.grid(row=1, column=4)

multiply = Button(frame, text='x', width=9, height=4, font=35, command=lambda: button_press('*'))
multiply.grid(row=2, column=4)

divide = Button(frame, text='/', width=9, height=4, font=35, command=lambda: button_press('/'))
divide.grid(row=3, column=4)

# create equals button

equal = Button(frame, text='=', width=9, height=4, font=35, command=equals)
equal.grid(row=3, column=2)

# create decimal button
decimal = Button(frame, text='.', width=9, height=4, font=35, command=lambda: button_press('.'))
decimal.grid(row=3, column=1)

# create clear button
clear = Button(window, text='clear', width=12, height=4, font=35, command=clear)
clear.pack()

window.mainloop()
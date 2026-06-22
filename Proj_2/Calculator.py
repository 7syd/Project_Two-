import tkinter as tk

root = tk.Tk()

root.title("Calculator")
root.geometry("420x700")
root.configure(bg="black")
root.resizable(False, False)




# Functions 


def button_click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(value))

def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")


def percentage():
    try:
        value = float(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(value / 100))
    except:
        pass

# added floor division if required but most calculators layout do not have that

def backspace():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])


def toggle_sign():
    current = display.get()

    if not current:
        return

    try:
        value = float(current)

        if value > 0:
            display.delete(0, tk.END)
            display.insert(0, "-" + current)

        elif value < 0:
            display.delete(0, tk.END)
            display.insert(0, current[1:])

    except:
        pass

def key_press(event):
    key = event.char

    if key in "0123456789+-*/.":
        button_click(key)

    elif event.keysym == "Return":
        calculate()

    elif event.keysym == "BackSpace":
        current = display.get()
        display.delete(0, tk.END)
        display.insert(0, current[:-1])

    elif event.keysym in ["Return", "KP_Enter"]:
        calculate()


display = tk.Entry(
    root,
    font=("Arial", 48),
    bg="black",
    fg="white",
    bd=0,
    justify="right",
    insertbackground="white"
)

display.pack(fill="x", padx=20, pady=(40,20), ipady=25)
# display.focus_set()
display.bind("<Key>", lambda e: "break")



buttons = [
    ["C", "+/-", "%", "⌫"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

button_frame = tk.Frame(root, bg="black")
for row in buttons:
    row_frame = tk.Frame(button_frame, bg="black")
    row_frame.pack(expand=True, fill="both")
    root.focus_set()

    for btn in row:
        
        if btn in ["+", "-", "*", "/", "="]:
            bg_color = "#FF9F0A"
            fg_color = "white"

        elif btn in ["C", "+/-", "%"]:
            bg_color = "#A5A5A5"
            fg_color = "black"

        else:
            bg_color = "#333333"
            fg_color = "white"

        action = lambda x=btn: button_click(x)

        if btn == "C":
            action = clear_display

        elif btn == "+/-":
            action = toggle_sign

        elif btn == "%":
            action = percentage

        elif btn == "=":
            action = calculate

        elif btn == "⌫":
            action = backspace

        button = tk.Button(
            row_frame,
            text=btn,
            font=("Arial", 26),
            bg=bg_color,
            fg=fg_color,
            bd=0,
            command=action
        )

        button.pack(side="left", expand=True, fill="both", padx=4, pady=4)

button_frame.pack(expand=True, fill="both")

root.bind_all("<Key>", key_press)


footer = tk.Label(
    root,
    # text="Created using Python & Tkinter",
    bg="black",
    fg="gray"
)

footer.pack(pady=5)

root.mainloop()
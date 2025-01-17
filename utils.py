import tkinter as tk

def customMessagebox(parent, title, message):
    top = tk.Toplevel(parent)
    top.title(title)

    label = tk.Label(top, text=message, font=("Arial", 16), wraplength=350, justify="left", anchor="w")
    label.pack(padx=20, pady=20, fill="x", anchor="w")

    ok_button = tk.Button(top, text="OK", font=("Arial", 14), command=top.destroy)
    ok_button.pack(pady=10)

    top.transient(parent)
    top.grab_set()
    parent.wait_window(top)


def textBox(parent, text, row, column=0):
    label = tk.Label(parent, text=text, font=("Arial", 16), justify="left", anchor="w")
    label.grid(row=row * 2 - 1, column=column, padx=35, pady=2, sticky="w")
    entry = tk.Entry(parent, width=80, font=("Arial", 16))
    entry.grid(row=row * 2, column=column, padx=25, pady=(0,8))
    return entry
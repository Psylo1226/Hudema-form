import tkinter as tk
from tkinter import messagebox, ttk


def display_text():
    inputs = [ent.get() for ent in entries]
    messagebox.showinfo("Wybrane wartości", "\n".join(f"{text_fields[i]}: {value}" for i, value in enumerate(inputs)))


def text_box(parent, text, row, column=0):
    label = tk.Label(parent, text=text)
    label.grid(row=row * 2 - 1, column=column, padx=10, pady=5)
    entry = tk.Entry(parent, width=80)
    entry.grid(row=row * 2, column=column, padx=10, pady=5)
    return entry


root = tk.Tk()
root.title("LLama")


entries = []
text_fields = ["Tytuł", "Tematyka", "Poziom zainteresowania"]

for index, text in enumerate(text_fields, start=1):
    entry = text_box(root, text, index)
    entries.append(entry)

submit_button = tk.Button(root, text="Submit", command=display_text)
submit_button.grid(row=len(text_fields) * 2 + 1, column=0, columnspan=2, pady=10)

root.update_idletasks()
width = root.winfo_reqwidth()
height = root.winfo_reqheight()
root.geometry(f"{width}x{height}")
icon = tk.PhotoImage(file="images/icon.png")
root.iconphoto(True, icon)

# Run the application
root.mainloop()

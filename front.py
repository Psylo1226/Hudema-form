import tkinter as tk
from tkinter import messagebox
from utils import customMessagebox,textBox
from resultScreen import resultBox

root = tk.Tk()
root.title("LLama")


entries = []
text_fields = ["Tytuł", "Tematyka", "Poziom zainteresowania"]

for index, text in enumerate(text_fields, start=1):
    entry = textBox(root, text, index)
    entries.append(entry)

def submitResults():
    resultBox(root, entries, text_fields)

submit_button = tk.Button(root, text="Prześlij", command=submitResults, font=("Arial", 16))
submit_button.grid(row=len(text_fields) * 2 + 1, column=0, columnspan=2, pady=10)

root.update_idletasks()
width = root.winfo_reqwidth()
height = root.winfo_reqheight()
root.geometry(f"{width}x{height}")
icon = tk.PhotoImage(file="images/icon.png")
root.iconphoto(True, icon)

# Run the application
root.mainloop()

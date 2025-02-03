import tkinter as tk
from tkinter import messagebox

from logic import recommend_course
from utils import customMessagebox,textBox
from resultScreen import resultBox

root = tk.Tk()
root.title("Formularz")


entries = []
text_fields = ["Tytuł", "Tematyka", "Poziom zainteresowania"]

for index, text in enumerate(text_fields, start=1):
    entry = textBox(root, text, index)
    entries.append(entry)

def submitResults():
    user_input = " ".join(entry.get() for entry in entries)
    recommended_course = recommend_course(user_input)
    resultBox(root, recommended_course)  # Przekazujemy tylko nazwę kursu

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

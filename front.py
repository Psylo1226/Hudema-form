import tkinter as tk
from tkinter import messagebox

from logic import recommend_course
from utils import customMessagebox,textBox
from resultScreen import resultBox

root = tk.Tk()
root.title("Formularz")


entries = []
text_fields = ["Szukana tematyka", "Posiadane umiejętności", "Poziom zaawansowania"]

for index, text in enumerate(text_fields, start=1):
    entry = textBox(root, text, index)
    entries.append(entry)

def submitResults():
    search_topic = entries[0].get()  # Tytuł kursu lub jego temat
    search_skills = entries[1].get()  # Posiadane umiejętności
    search_level = entries[2].get()  # Pożądany poziom

    # Pobranie rekomendowanego kursu
    recommended_course, course_goals, course_program = recommend_course(search_topic, search_skills, search_level)

    # Wywołanie okna wyników
    resultBox(root, recommended_course, course_goals, course_program)


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

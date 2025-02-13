import tkinter as tk
from logic import recommend_course
from utils import textBox,ParticleBackground

root = tk.Tk()
root.title("🚀 Formularz")
root.configure(bg="#343a40")  
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")  


bg = ParticleBackground(root, root.winfo_screenwidth(), root.winfo_screenheight(), 100)


main_frame = tk.Frame(root, bg="white", bd=3, relief="solid")
main_frame.place(relx=0.5, rely=0.5, anchor="center", width=root.winfo_screenwidth() * 0.6, height=root.winfo_screenheight() * 0.7)

form_frame = tk.Frame(main_frame, bg="white")
form_frame.pack(fill="both", expand=True, padx=30, pady=20)

entries = []
text_fields = ["Szukana tematyka", "Posiadane umiejętności", "Poziom zaawansowania"]

for index, text in enumerate(text_fields, start=1):
    entry = textBox(form_frame, text, index)
    entries.append(entry)

# 📌 Efekty hover i kliknięcia dla przycisków
def on_enter(e):
    e.widget.config(bg="#218838")  # Ciemniejszy zielony

def on_leave(e):
    e.widget.config(bg="#28a745")  # Jasny zielony

def close_on_enter(e):
    e.widget.config(bg="#c82333")  # Ciemniejszy czerwony

def close_on_leave(e):
    e.widget.config(bg="#dc3545")  # Jasny czerwony

# 📌 Funkcja do wyświetlania wyników
def show_results(course_name, course_goals, course_program):
    global result_frame

    # Usuwanie poprzednich wyników, jeśli istnieją
    if hasattr(root, "result_frame"):
        root.result_frame.destroy()

    # Tworzenie ramki na wyniki
    result_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid")
    result_frame.pack(fill="both", expand=True, padx=20, pady=10)
    root.result_frame = result_frame

    # Tworzenie scrollbara dla długich wyników
    canvas = tk.Canvas(result_frame, bg="white", highlightthickness=0)
    scrollbar = tk.Scrollbar(result_frame, orient="vertical", command=canvas.yview)

    scroll_frame = tk.Frame(canvas, bg="white")

    scroll_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scroll_frame, anchor="nw", width=root.winfo_screenwidth() - 150)
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Nagłówek kursu
    tk.Label(
        scroll_frame,
        text=course_name,
        font=("Arial", 22, "bold"),
        fg="#343a40",
        bg="white",
        wraplength=root.winfo_screenwidth() * 0.5,  # Maksymalna szerokość = 50% ekranu
        justify="center"  # Wyśrodkowanie tekstu
    ).pack(pady=10, padx=20, anchor="w")

    # Cele kursu
    tk.Label(
        scroll_frame,
        text="🎯 Cele kursu:",
        font=("Arial", 16, "bold"),
        fg="#007bff",
        bg="white"
    ).pack(anchor="w", padx=20, pady=(10, 0))

    goals_label = tk.Label(
        scroll_frame,
        text=course_goals,
        font=("Arial", 14),
        fg="#495057",
        bg="white",
        wraplength=root.winfo_screenwidth() * 0.5,
        justify="left"
    )
    goals_label.pack(anchor="w", padx=20, pady=5)

    # Program kursu
    tk.Label(
        scroll_frame,
        text="📚 Program kursu:",
        font=("Arial", 16, "bold"),
        fg="#28a745",
        bg="white"
    ).pack(anchor="w", padx=20, pady=(10, 0))

    program_label = tk.Label(
        scroll_frame,
        text=course_program,
        font=("Arial", 14),
        fg="#495057",
        bg="white",
        wraplength=root.winfo_screenwidth() * 0.5,
        justify="left"
    )
    program_label.pack(anchor="w", padx=20, pady=5)

    # Przycisk zamknięcia wyników
    close_button = tk.Button(
        scroll_frame,
        text="❌ Zamknij",
        font=("Arial", 14, "bold"),
        bg="#dc3545",
        fg="white",
        relief="flat",
        padx=15,
        pady=8,
        command=lambda: close_results()
    )
    close_button.pack(pady=10, padx=20, anchor="w")

    close_button.bind("<Enter>", close_on_enter)
    close_button.bind("<Leave>", close_on_leave)

# 📌 Funkcja zamykająca wyniki
def close_results():
    if hasattr(root, "result_frame"):
        root.result_frame.destroy()


def submitResults():
    search_topic = entries[0].get()
    search_skills = entries[1].get()
    search_level = entries[2].get()
    
    recommended_course, course_goals, course_program = recommend_course(search_topic, search_skills, search_level)
    show_results(recommended_course, course_goals, course_program)


# Przycisk "Prześlij"
submit_button = tk.Button(
    form_frame,
    text="🚀 Prześlij",
    command=submitResults,
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#28a745",
    activebackground="#218838",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=8,
    bd=3,
    cursor="hand2"
)
submit_button.grid(row=len(text_fields) * 2 + 1, column=0, columnspan=2, pady=20, ipadx=15, ipady=8)
submit_button.bind("<Enter>", on_enter)
submit_button.bind("<Leave>", on_leave)


root.update_idletasks()
root.state("zoomed")  # Pełnoekranowe okno

try:
    icon = tk.PhotoImage(file="images/icon.png")
    root.iconphoto(True, icon)
except Exception as e:
    print("⚠ Nie znaleziono pliku ikonki:", e)

root.mainloop()

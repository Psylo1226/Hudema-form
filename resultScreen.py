import tkinter as tk
from tkinter import messagebox
from utils import customMessagebox,textBox


def resultBox(parent, course_name, course_goals, course_program):
    result_window = tk.Toplevel(parent)
    result_window.title("Polecany kurs")

    # Nagłówek z nazwą kursu
    title_label = tk.Label(result_window, text=course_name, font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    # Kontener na szczegóły kursu (ukryty na starcie)
    details_frame = tk.Frame(result_window)

    # Cele kursu
    tk.Label(details_frame,text="Cele kursu:\n", font=("Arial", 13), justify="left").pack()
    goals_label = tk.Label(details_frame, text=f"{course_goals}", font=("Arial", 10), justify="left",
                           wraplength=1200)
    goals_label.pack(pady=(0,5))

    # Program kursu
    tk.Label(details_frame, text="Program kursu:\n", font=("Arial", 13), justify="left").pack()
    program_label = tk.Label(details_frame, text=f"{course_program}", font=("Arial", 10),
                             justify="left", wraplength=1200)
    program_label.pack(pady=(0,5))

    # Funkcja do rozwijania i zwijania szczegółów
    def toggle_details():
        if details_frame.winfo_ismapped():
            details_frame.pack_forget()
            toggle_button.config(text="Pokaż więcej")
        else:
            details_frame.pack(pady=5)
            toggle_button.config(text="Ukryj")

    # Przycisk do rozwijania
    toggle_button = tk.Button(result_window, text="Pokaż więcej", command=toggle_details, font=("Arial", 12))
    toggle_button.pack(pady=5)

    # Zamknięcie okna
    close_button = tk.Button(result_window, text="Zamknij", command=result_window.destroy, font=("Arial", 12))
    close_button.pack(pady=5)




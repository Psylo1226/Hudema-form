import tkinter as tk
from tkinter import messagebox
from utils import customMessagebox,textBox

def resultBox(parent, recommended_course):
    customMessagebox(parent, "Polecany kurs", f"Najlepiej dopasowany kurs: {recommended_course}")



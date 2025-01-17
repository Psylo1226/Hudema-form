import tkinter as tk
from tkinter import messagebox
from utils import customMessagebox,textBox

def resultBox(parent,entries,text_fields):
    inputs = [ent.get() for ent in entries]
    customMessagebox(parent,"Wybrane wartości", "\n".join(f"{text_fields[i]}: {value}" for i, value in enumerate(inputs)))



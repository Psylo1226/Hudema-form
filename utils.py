import tkinter as tk
import random

def customMessagebox(parent, title, message):
    # Tworzenie nowego okna
    top = tk.Toplevel(parent)
    top.title(title)
    top.configure(bg="#f8f9fa") 
    frame = tk.Frame(top, bg="white", bd=2, relief="solid")
    frame.pack(padx=20, pady=20, fill="both", expand=True)

    title_label = tk.Label(
        frame,
        text=title,
        font=("Arial", 18, "bold"),
        fg="#343a40",
        bg="white",
        pady=10
    )
    title_label.pack()

    message_label = tk.Label(
        frame,
        text=message,
        font=("Arial", 14),
        fg="#495057",
        bg="white",
        wraplength=350,
        justify="left"
    )
    message_label.pack(padx=15, pady=10)

    ok_button = tk.Button(
        frame,
        text="✅ OK",
        font=("Arial", 14, "bold"),
        fg="white",
        bg="#007bff",
        relief="flat",
        padx=10,
        pady=5,
        command=top.destroy
    )
    ok_button.pack(pady=15)

    top.transient(parent)
    top.grab_set()
    parent.wait_window(top)


def textBox(parent, text, row, column=0):
    
    label = tk.Label(
        parent,
        text=text,
        font=("Arial", 14, "bold"),
        fg="#495057",
        bg="#f8f9fa",
        justify="left",
        anchor="w"
    )
    label.grid(row=row * 2 - 1, column=column, padx=20, pady=5, sticky="w")

    entry = tk.Entry(
        parent,
        width=50,
        font=("Arial", 14),
        fg="#212529",
        bg="white",
        bd=2,
        relief="solid",
        highlightthickness=1,
        highlightbackground="#ced4da",
        highlightcolor="#007bff"
    )
    entry.grid(row=row * 2, column=column, padx=20, pady=(0, 10), ipadx=5, ipady=7)

    return entry
class Particle:
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.size = random.randint(3, 7)
        self.dx = random.uniform(-1, 1)
        self.dy = random.uniform(-1, 1)

        self.id = canvas.create_oval(
            self.x, self.y, self.x + self.size, self.y + self.size, 
            fill="white", outline=""
        )

    def move(self, width, height):
        self.x += self.dx
        self.y += self.dy

        if self.x < 0: self.x = width
        if self.x > width: self.x = 0
        if self.y < 0: self.y = height
        if self.y > height: self.y = 0

        self.canvas.move(self.id, self.dx, self.dy)

class ParticleBackground:
    def __init__(self, root, width, height, num_particles=100):
        self.width = width
        self.height = height
        self.canvas = tk.Canvas(root, width=width, height=height, bg="#343a40", highlightthickness=0)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)

        self.particles = [Particle(self.canvas, width, height) for _ in range(num_particles)]
        self.animate()

    def animate(self):
        for particle in self.particles:
            particle.move(self.width, self.height)
        self.canvas.after(30, self.animate)

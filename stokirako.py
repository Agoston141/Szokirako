import tkinter as tk
import random

class Szokirako:
    def __init__(self, root):
        self.root = root
        self.root.title("Szókirakó")
        self.root.geometry("400x250")
        self.szavak = ["alma", "körte", "barack", "szilva", "eper"]  # Példaként néhány szó

        self.kitalalandóSzo = random.choice(self.szavak)

        self.szoveg_label = tk.Label(self.root, text=self.kitalalandóSzo, font=("Arial", 24))
        self.szoveg_label.pack(pady=20)

        self.megoldas_entry = tk.Entry(self.root, font=("Arial", 24))
        self.megoldas_entry.pack(pady=10)

        self.ellenorzes_btn = tk.Button(self.root, text="Ellenőrzés", command=self.ellenorzes)
        self.ellenorzes_btn.pack(pady=10)

    def ellenorzes(self):
        megoldas = self.megoldas_entry.get()
        if megoldas == self.kitalalandóSzo:
            eredmeny = "Gratulálok, helyes megoldás!"
        else:
            eredmeny = "Sajnálom, rossz megoldás."

        ellenorzes_eredmeny_label = tk.Label(self.root, text=eredmeny, font=("Arial", 18))
        ellenorzes_eredmeny_label.pack(pady=10)

root = tk.Tk()
app = Szokirako(root)
root.mainloop()
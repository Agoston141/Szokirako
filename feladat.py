import tkinter as tk
from random import choice, shuffle
from time import time

class BetuvarazsJatek:
    def __init__(self, root):
        self.root = root
        self.root.title("Betűvarázs Játék")

        self.pontszam = 0
        self.remaining_time = 60
        self.szavak = ["alma", "körte", "barack", "eper", "citrom", "szilva", "narancs", "szőlő", "dinnye", "meggy"]
        self.aktualis_szo = ""

        self.keszit_ui()
        self.kovetkezo_szo()

    def keszit_ui(self):
        self.lbl_pontszam = tk.Label(self.root, text="Pontszám: 0", font=("Helvetica", 16))
        self.lbl_pontszam.pack(pady=10)

        self.lbl_szoveg = tk.Label(self.root, text="", font=("Helvetica", 24))
        self.lbl_szoveg.pack(pady=20)

        self.entry_tipp = tk.Entry(self.root, font=("Helvetica", 18))
        self.entry_tipp.pack(pady=10)

        self.btn_tippel = tk.Button(self.root, text="Tippelés", command=self.ellenoriz_tippet)
        self.btn_tippel.pack(pady=10)

        self.lbl_hatralevo_ido = tk.Label(self.root, text="Idő: 60", font=("Helvetica", 16))
        self.lbl_hatralevo_ido.pack(pady=10)

        self.root.after(1000, self.csokkent_idot)

    def kovetkezo_szo(self):
        self.aktualis_szo = choice(self.szavak)
        betuk = list(self.aktualis_szo)
        shuffle(betuk)
        self.lbl_szoveg.config(text=" ".join(betuk))
        self.entry_tipp.delete(0, tk.END)

    def ellenoriz_tippet(self):
        tipp = self.entry_tipp.get().lower()
        if tipp == self.aktualis_szo:
            self.pontszam += 1
            self.lbl_pontszam.config(text="Pontszám: {}".format(self.pontszam))
        self.kovetkezo_szo()

    def csokkent_idot(self):
        self.remaining_time -= 1
        self.lbl_hatralevo_ido.config(text="Idő: {}".format(self.remaining_time))

        if self.remaining_time > 0:
            self.root.after(1000, self.csokkent_idot)
        else:
            self.lbl_hatralevo_ido.config(text="Idő: 0")
            self.btn_tippel.config(state=tk.DISABLED)
            self.entry_tipp.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    jatek = BetuvarazsJatek(root)
    root.mainloop()

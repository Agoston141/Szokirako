import tkinter as tk
from random import choice, shuffle
from time import time

class BetuvarazsJatek:
    #Alap beállÍtások:
    def __init__(self, root):
        self.root = root
        self.root.title("Betűvarázs Játék")
        self.root.configure(bg="antiquewhite")
        self.root.geometry("500x400")

        self.pontszam = 0
        self.remaining_time = 30
        self.szavak = ["ászok", "bűzös", "csősz", "díszes", "gyáva", "hossz", "üzlet", "nyert", "egész", "álmos","mézes", "nézés", "szuri", "kocsi", "madár", "rázás", "sávot", "tisza", "úszás", "szóda","zörgő", "ázott", "búzás", "virág", "edény", "gyűjt", "kulcs", "lámpa", "szita", "arany","lövés", "sózza", "nővér", "tiszt", "kosár", "párna", "keres", "tézis", "munka", "kerék","dongó", "elkap", "bűzös", "csepp", "mókás", "gyárt", "lőtér", "fagyi", "illat", "három","hárem", "kérés", "főtér", "csoki", "eltör", "zárás", "dobál", "futás", "balhé", "keret","morgó", "margó", "ágyas", "csepp", "aktív", "alany", "álarc", "alant", "ágyás", "kézír","akció", "aláír", "zsuga", "zuzmó", "zúgás", "zseni", "zavar", "zárva", "zajos", "zokni","zamat", "zuhog", "bácsi", "bajos", "banya", "bárka", "barna", "beáll", "befőz", "belép","bendő", "békés", "bókol", "borul", "borsó", "bimbó", "balta", "lakos", "látás", "lazac","leány", "lázas", "lebeg", "lakás", "labda", "leves", "linux", "liter", "lóbőr", "létra","lepel", "lepra", "lóbab", "lóerő", "mangó", "meder", "megöl", "magán", "magas", "mágia","magol", "mámor", "majom", "mókus", "méter", "manus", "málna", "mankó", "mappa", "meggy","méhfű", "meleg", "ménes", "menta", "menza", "méreg", "mérés", "sajtó", "sámli", "sarok","sánta", "segéd", "sofőr", "sóher", "smink", "sógor", "kalap", "kabát", "kábel", "kabin","kábít", "kajak", "kakaó", "káosz", "kaspó", "kelta", "kefél", "karát", "kapor", "keksz","pacal", "páclé", "páros", "pacák", "pakli", "pedál", "plüss", "pohár", "póker", "posta","préda", "púder", "puska", "pózna", "ganéj", "gatya", "garbó", "garas", "garat", "gipsz","görcs", "gyűrű", "gyufa", "gőzös", "gitár", "gazda", "dagad", "derék", "dühös", "dráma","drága", "donor", "dohos", "donga", "radar", "randi", "rakás", "rúdfa", "repül", "vacak","vádli", "vaksi", "vágás", "vasal", "veréb", "vezér", "ideál", "igény", "index", "inger","intim", "ionos", "ipari", "iroda", "izmos", "iszik", "faarc", "félév", "fazon", "fahéj","faláb", "felhő", "farol", "nádas", "nagyi", "napos", "nemes", "nomád", "nyárs", "nimfa","nézés", "bánat", "űrlap", "illat", "őrház", "őrség", "őszül", "őzhús", "őskor", "óceán","óvoda", "ókori", "ópium", "előke", "edzés", "egyke", "egyén", "eposz", "esély", "enzim"]
        self.aktualis_szo = ""

        self.keszit_ui()
        self.random_szo()

    #A pogram megjelenése
    def keszit_ui(self):
        self.lbl_pontszam = tk.Label(self.root, text="Pontszám: 0", font=("Helvetica", 16),background=("antiquewhite"))
        self.lbl_pontszam.pack(pady=10)

        self.lbl_szoveg = tk.Label(self.root, text="", font=("Helvetica", 24),background=("antiquewhite"))
        self.lbl_szoveg.pack(pady=20)

        self.entry_tipp = tk.Entry(self.root, font=("Helvetica", 18),)
        self.entry_tipp.pack(pady=10,)

        self.btn_tippel = tk.Button(self.root, text="Tippelés", command=self.ellenoriz_tippet, cursor=("hand2"))
        self.btn_tippel.pack(pady=10)

        self.lbl_hatralevo_ido = tk.Label(self.root, text="Idő: 30", font=("Helvetica", 16),background=("antiquewhite"))
        self.lbl_hatralevo_ido.pack(pady=10)

        self.root.after(1000, self.csokkent_idot)
    
    #A random szavakat létrehozza
    def random_szo(self):
        self.aktualis_szo = choice(self.szavak)
        betuk = list(self.aktualis_szo)
        shuffle(betuk)
        self.lbl_szoveg.config(text=" ".join(betuk))
        self.entry_tipp.delete(0, tk.END)

    #Ellenőrzi a tippet
    def ellenoriz_tippet(self):
        tipp = self.entry_tipp.get().lower()
        if tipp == self.aktualis_szo:
            self.pontszam += 1
            self.lbl_pontszam.config(text="Pontszám: {}".format(self.pontszam))
        self.random_szo()

    #Az időt csökkenti és ha lejár az idő mindent "DISABLED"-re állÍt
    def csokkent_idot(self):
        self.remaining_time -= 1
        self.lbl_hatralevo_ido.config(text="Idő: {}".format(self.remaining_time))

        if self.remaining_time > 0:
            self.root.after(1000, self.csokkent_idot)
        else:
            self.lbl_hatralevo_ido.config(text="Idő: 0")
            self.btn_tippel.config(state=tk.DISABLED,cursor=("arrow"))
            self.entry_tipp.config(state=tk.DISABLED)
            self.lbl_szoveg.config(text="Az idő lejárt!\nJáték vége!")


if __name__ == "__main__":
    root = tk.Tk()
    jatek = BetuvarazsJatek(root)
    root.mainloop()

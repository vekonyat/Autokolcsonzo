
class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []
        self.ugyfelek = []

    def auto_hozzaad(self, auto):
        self.autok.append(auto)

    def ugyfel_hozzaad(self, ugyfel):
        self.ugyfelek.append(ugyfel)

    def berles_hozzaad(self, berles):
        self.berlesek.append(berles)

    def __str__(self):
        return f"{self.nev} car rent - Rent a car!"

    def berlesek_listazasa(self):
        if not self.berlesek:
            print("Jelenleg nincsenek aktív bérlések.")
        else:
            for berles in self.berlesek:
                print(berles)




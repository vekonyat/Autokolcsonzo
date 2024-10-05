from Berles import Berles


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

    def berles_hozzaadasa(self, auto, datum, ugyfel):
        for berles in self.berlesek:
            if berles.auto.rendszam == auto.rendszam and berles.datum == datum:
                print(f"Van már bérlés a megadott időpontra {auto.rendszam} rendszámmal.")
                return False
        uj_id = len(self.berlesek) + 1
        uj_berles = Berles(uj_id, auto, datum, ugyfel)
        self.berlesek.append(uj_berles)
        print(f"Sikeres bérlés: {auto.rendszam} - {auto.tipus} bérelve {datum} dátumra {ugyfel.name} számára.")
        return True

    def berles_lemondasa(self, id):
        for berles in self.berlesek:
            if berles.id == id:
                self.berlesek.remove(berles)
                print(f"Bérlés lemondva: {berles.auto.rendszam} - {berles.auto.tipus}.")
                return True
        print(f"Nincs bérlés a megadott ID-val: {id}.")
        return False



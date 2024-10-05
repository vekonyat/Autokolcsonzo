
class Berles:
    def __init__(self, id, auto, datum, ugyfel):
        self.id = id
        self.auto = auto
        self.datum = datum
        self.ugyfel = ugyfel

    def __str__(self):
        return f"ID: {self.id}, Bérlés: {self.auto.rendszam} - {self.auto.tipus}, Dátum: {self.datum}, Ügyfél: {self.ugyfel}, Ár: {self.auto.berleti_dij} Ft"

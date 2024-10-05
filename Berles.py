
class Berles:
    def __init__(self, auto, datum, ugyfel):
        self.auto = auto
        self.datum = datum
        self.ugyfel = ugyfel

    def __str__(self):
        return f"Bérlés: {self.auto.rendszam} - {self.auto.tipus}, Dátum: {self.datum}, Ügyfél: {self.ugyfel}"
